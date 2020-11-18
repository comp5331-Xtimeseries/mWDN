# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/003b_data.transforms.ipynb (unless otherwise specified).

__all__ = ['TSIdentity', 'TSShuffle_HLs', 'TSShuffleSteps', 'TSMagAddNoise', 'TSMagMulNoise', 'random_curve_generator',
           'random_cum_curve_generator', 'random_cum_noise_generator', 'random_cum_linear_generator', 'TSTimeNoise',
           'TSMagWarp', 'TSTimeWarp', 'TSWindowWarp', 'TSMagScale', 'TSMagScalePerVar', 'TSRandomResizedCrop',
           'TSRandomZoomIn', 'TSWindowSlicing', 'TSRandomZoomOut', 'TSRandomTimeScale', 'TSRandomTimeStep', 'TSBlur',
           'TSSmooth', 'maddest', 'TSFreqDenoise', 'TSRandomFreqNoise', 'TSRandomResizedLookBack', 'TSVarOut',
           'TSCutOut', 'TSTimeStepOut', 'TSRandomCropPad', 'TSMaskOut', 'TSTranslateX', 'TSRandomShift',
           'TSHorizontalFlip', 'TSRandomTrend', 'TSRandomRotate', 'TSVerticalFlip', 'TSResize', 'TSRandomSize',
           'TSRandomLowRes', 'TSDownUpScale', 'TSRandomDownUpScale', 'all_TS_randaugs', 'RandAugment', 'TestTfm',
           'get_tfm_name']

# Cell
from fastai.vision.augment import RandTransform
from ..imports import *
from ..utils import *
from .external import *
from .core import *
from .preprocessing import *

# Cell
from scipy.interpolate import CubicSpline
from scipy.ndimage import convolve1d, zoom
import pywt
from pyts.image.gaf import GramianAngularField

# Cell
class TSIdentity(RandTransform):
    "Applies the identity tfm to a `TSTensor` batch"
    order = 90
    def __init__(self, magnitude=None, **kwargs):
        self.magnitude = magnitude
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)): return o

# Cell
# partial(TSShuffle_HLs, ex=0),
class TSShuffle_HLs(RandTransform):
    "Randomly shuffles HIs/LOs of an OHLC `TSTensor` batch"
    order = 70
    def __init__(self, magnitude=1., ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        timesteps = o.shape[-1] // 4
        pos_rand_list = np.random.choice(np.arange(timesteps),size=random.randint(1, timesteps),replace=False)
        rand_list = pos_rand_list * 4
        highs = rand_list + 1
        lows = highs + 1
        a = np.vstack([highs, lows]).flatten('F')
        b = np.vstack([lows, highs]).flatten('F')
        output = o.clone()
        output[...,a] = output[...,b]
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
# partial(TSShuffleSteps, ex=0),
class TSShuffleSteps(RandTransform):
    "Randomly shuffles consecutive sequence datapoints in batch"
    order = 70
    def __init__(self, magnitude=1., ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        odd = 1 - o.shape[-1]%2
        r = np.random.randint(2)
        timesteps = o.shape[-1] // 2
        pos_rand_list = np.random.choice(np.arange(0, timesteps - r * odd), size=random.randint(1, timesteps - r * odd),replace=False) * 2 + 1 + r
        a = np.vstack([pos_rand_list, pos_rand_list - 1]).flatten('F')
        b = np.vstack([pos_rand_list - 1, pos_rand_list]).flatten('F')
        output = o.clone()
        output[...,a] = output[...,b]
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSMagAddNoise(RandTransform):
    "Applies additive noise on the y-axis for each step of a `TSTensor` batch"
    order = 80
    def __init__(self, magnitude=1, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        # output = o + torch.normal(0, o.std() * self.magnitude, o.shape, dtype=o.dtype, device=o.device)
        output = o + torch.normal(0, 1/3, o.shape, dtype=o.dtype, device=o.device) * (o[..., 1:] - o[..., :-1]).std(2, keepdims=True) * self.magnitude
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

class TSMagMulNoise(RandTransform):
    "Applies multiplicative noise on the y-axis for each step of a `TSTensor` batch"
    order = 80
    def __init__(self, magnitude=1, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        noise = torch.normal(1, self.magnitude * .025, o.shape, dtype=o.dtype, device=o.device)
        output = o * noise
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
def random_curve_generator(o, magnitude=0.1, order=4, noise=None):
    seq_len = o.shape[-1]
    f = CubicSpline(np.linspace(-seq_len, 2 * seq_len - 1, 3 * (order - 1) + 1, dtype=int),
                    np.random.normal(loc=1.0, scale=magnitude, size=3 * (order - 1) + 1), axis=-1)
    return f(np.arange(seq_len))

def random_cum_curve_generator(o, magnitude=0.1, order=4, noise=None):
    x = random_curve_generator(o, magnitude=magnitude, order=order, noise=noise).cumsum()
    x -= x[0]
    x /= x[-1]
    x = np.clip(x, 0, 1)
    return x * (o.shape[-1] - 1)

def random_cum_noise_generator(o, magnitude=0.1, noise=None):
    seq_len = o.shape[-1]
    x = np.clip(np.ones(seq_len) + np.random.normal(loc=0, scale=magnitude, size=seq_len), 0, 1000).cumsum()
    x -= x[0]
    x /= x[-1]
    return x * (o.shape[-1] - 1)

def random_cum_linear_generator(o, magnitude=0.1):
    seq_len = o.shape[-1]
    win_len = int(round(seq_len * np.random.rand() * magnitude))
    if win_len == seq_len: return np.arange(o.shape[-1])
    start = np.random.randint(0, seq_len - win_len)
    # mult between .5 and 2
    rand = np.random.rand()
    mult = 1 + rand
    if np.random.randint(2): mult = 1 - rand/2
    x = np.ones(seq_len)
    x[start : start + win_len] = mult
    x = x.cumsum()
    x -= x[0]
    x /= x[-1]
    return np.clip(x, 0, 1) * (seq_len - 1)

# Cell
class TSTimeNoise(RandTransform):
    "Applies noise to each step in the x-axis of a `TSTensor` batch based on smooth random curve"
    order = 80
    def __init__(self, magnitude=0.1, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        f = CubicSpline(np.arange(o.shape[-1]), o.cpu(), axis=-1)
        output = o.new(f(random_cum_noise_generator(o, magnitude=self.magnitude)))
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSMagWarp(RandTransform):
    "Applies warping to the y-axis of a `TSTensor` batch based on a smooth random curve"
    order = 80
    def __init__(self, magnitude=0.02, ord=4, ex=None, **kwargs):
        self.magnitude, self.ord, self.ex = magnitude, ord, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if self.magnitude and self.magnitude <= 0: return o
        y_mult = random_curve_generator(o, magnitude=self.magnitude, order=self.ord)
        output = o * o.new(y_mult)
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSTimeWarp(RandTransform):
    "Applies time warping to the x-axis of a `TSTensor` batch based on a smooth random curve"
    order = 80
    def __init__(self, magnitude=0.02, ord=4, ex=None, **kwargs):
        self.magnitude, self.ord, self.ex = magnitude, ord, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        f = CubicSpline(np.arange(o.shape[-1]), o.cpu(), axis=-1)
        output = o.new(f(random_cum_curve_generator(o, magnitude=self.magnitude, order=self.ord)))
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSWindowWarp(RandTransform):
    """Applies window slicing to the x-axis of a `TSTensor` batch based on a random linear curve based on
    https://halshs.archives-ouvertes.fr/halshs-01357973/document"""
    order = 80
    def __init__(self, magnitude=0.1, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0 or self.magnitude >= 1: return o
        f = CubicSpline(np.arange(o.shape[-1]), o.cpu(), axis=-1)
        output = o.new(f(random_cum_linear_generator(o, magnitude=self.magnitude)))
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSMagScale(RandTransform):
    "Applies scaling to the y-axis of a `TSTensor` batch based on a scalar"
    order = 80
    def __init__(self, magnitude=0.5, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        rand = random_half_normal()
        scale = (1 - (rand  * self.magnitude)/2) if random.random() > 1/3 else (1 + (rand  * self.magnitude))
        output = o * scale
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

class TSMagScalePerVar(RandTransform):
    "Applies per_var scaling to the y-axis of a `TSTensor` batch based on a scalar"
    order = 80
    def __init__(self, magnitude=0.5, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        s = [1] * o.ndim
        s[-2] = o.shape[-2]
        rand = random_half_normal_tensor(s, device=o.device)
        scale = (1 - (rand  * self.magnitude)/2) if random.random() > 1/3 else (1 + (rand  * self.magnitude))
        output = o * scale
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSRandomResizedCrop(RandTransform):
    "Randomly amplifies a sequence focusing on a random section of the steps"
    order = 95
    def __init__(self, magnitude=0.1, ex=None, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.ex, self.mode = magnitude, ex, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        seq_len = o.shape[-1]
        lambd = np.random.beta(self.magnitude, self.magnitude)
        lambd = max(lambd, 1 - lambd)
        win_len = int(round(seq_len * lambd))
        if win_len == seq_len: return o
        start = np.random.randint(0, seq_len - win_len)
        return F.interpolate(o[..., start : start + win_len], size=seq_len, mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)

TSRandomZoomIn = TSRandomResizedCrop

# Cell
class TSWindowSlicing(RandTransform):
    "Randomly extracts an resize a ts slice based on https://halshs.archives-ouvertes.fr/halshs-01357973/document"
    order = 95
    def __init__(self, magnitude=0.1, ex=None, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.ex, self.mode = magnitude, ex, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0 or self.magnitude >= 1: return o
        seq_len = o.shape[-1]
        win_len = int(round(seq_len * (1 - self.magnitude)))
        if win_len == seq_len: return o
        start = np.random.randint(0, seq_len - win_len)
        return F.interpolate(o[..., start : start + win_len], size=seq_len, mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)

# Cell
class TSRandomZoomOut(RandTransform):
    "Randomly compresses a sequence on the x-axis"
    order = 95
    def __init__(self, magnitude=0.1, ex=None, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.ex, self.mode = magnitude, ex, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        seq_len = o.shape[-1]
        lambd = np.random.beta(self.magnitude, self.magnitude)
        lambd = max(lambd, 1 - lambd)
        win_len = int(round(seq_len * lambd))
        if win_len == seq_len: return o
        start = (seq_len - win_len) // 2
        output = torch.zeros_like(o, dtype=o.dtype, device=o.device)
        interp = F.interpolate(o, size=win_len, mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)
        output[..., start:start + win_len] = o.new(interp)
        return output

# Cell
class TSRandomTimeScale(RandTransform):
    "Randomly amplifies/ compresses a sequence on the x-axis keeping the same length"
    order = 95
    def __init__(self, magnitude=0.1, ex=None, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.ex, self.mode = magnitude, ex, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        if np.random.rand() <= 0.5: return TSRandomZoomIn(magnitude=self.magnitude, ex=self.ex, mode=self.mode)(o, split_idx=0)
        else: return TSRandomZoomOut(magnitude=self.magnitude, ex=self.ex, mode=self.mode)(o, split_idx=0)

# Cell
class TSRandomTimeStep(RandTransform):
    "Compresses a sequence on the x-axis by randomly selecting sequence steps and interpolating to previous size"
    order = 95
    def __init__(self, magnitude=0.02, ex=None, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.ex, self.mode = magnitude, ex, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        seq_len = o.shape[-1]
        new_seq_len = int(round(seq_len * max(.5, (1 - np.random.rand() * self.magnitude))))
        if  new_seq_len == seq_len: return o
        timesteps = np.sort(np.random.choice(np.arange(seq_len),new_seq_len, replace=False))
        output = F.interpolate(o[..., timesteps], size=seq_len, mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSBlur(RandTransform):
    "Blurs a sequence applying a filter of type [1, 0, 1]"
    order = 80
    def __init__(self, magnitude=1., ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        self.filterargs = np.array([1, 0, 1])
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        w = self.filterargs * np.random.rand(3)
        w = w / w.sum()
        output = o.new(convolve1d(o.cpu(), w, mode='nearest'))
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSSmooth(RandTransform):
    "Smoothens a sequence applying a filter of type [1, 5, 1]"
    order = 80
    def __init__(self, magnitude=1., ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        self.filterargs = np.array([1, 5, 1])
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        w = self.filterargs * np.random.rand(3)
        w = w / w.sum()
        output = o.new(convolve1d(o.cpu(), w, mode='nearest'))
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
def maddest(d, axis=None): #Mean Absolute Deviation
    return np.mean(np.absolute(d - np.mean(d, axis)), axis)

class TSFreqDenoise(RandTransform):
    "Denoises a sequence applying a wavelet decomposition method"
    order = 80
    def __init__(self, magnitude=0.1, ex=None, wavelet='db4', level=2, thr=None, thr_mode='hard', pad_mode='per', **kwargs):
        self.magnitude, self.ex = magnitude, ex
        self.wavelet, self.level, self.thr, self.thr_mode, self.pad_mode = wavelet, level, thr, thr_mode, pad_mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        """
        1. Adapted from waveletSmooth function found here:
        http://connor-johnson.com/2016/01/24/using-pywavelets-to-remove-high-frequency-noise/
        2. Threshold equation and using hard mode in threshold as mentioned
        in section '3.2 denoising based on optimized singular values' from paper by Tomas Vantuch:
        http://dspace.vsb.cz/bitstream/handle/10084/133114/VAN431_FEI_P1807_1801V001_2018.pdf
        """
        seq_len = o.shape[-1]
        # Decompose to get the wavelet coefficients
        coeff = pywt.wavedec(o.cpu(), self.wavelet, mode=self.pad_mode)
        # Calculate sigma for threshold as defined in http://dspace.vsb.cz/bitstream/handle/10084/133114/VAN431_FEI_P1807_1801V001_2018.pdf
        # As noted by @harshit92 MAD referred to in the paper is Mean Absolute Deviation not Median Absolute Deviation
        sigma = (1/0.6745) * maddest(coeff[-self.level])
        # Calculate the univeral threshold
        uthr = sigma * np.sqrt(2*np.log(seq_len)) * (1 if self.thr is None else self.magnitude)
        coeff[1:] = (pywt.threshold(c, value=uthr, mode=self.thr_mode) for c in coeff[1:])
        # Reconstruct the signal using the thresholded coefficients
        output = o.new(pywt.waverec(coeff, self.wavelet, mode=self.pad_mode)[..., :seq_len])
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSRandomFreqNoise(RandTransform):
    "Applys random noise using a wavelet decomposition method"
    order = 80
    def __init__(self, magnitude=0.1, ex=None, wavelet='db4', level=2, mode='constant', **kwargs):
        self.magnitude, self.ex = magnitude, ex
        self.wavelet, self.level, self.mode = wavelet, level, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        self.level = 1 if self.level is None else self.level
        coeff = pywt.wavedec(o.cpu(), self.wavelet, mode=self.mode, level=self.level)
        coeff[1:] = [c * (1 + 2 * (np.random.rand() - 0.5) * self.magnitude) for c in coeff[1:]]
        output = o.new(pywt.waverec(coeff, self.wavelet, mode=self.mode)[..., :o.shape[-1]])
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSRandomResizedLookBack(RandTransform):
    "Selects a random number of sequence steps starting from the end and return an output of the same shape"
    order = 95
    def __init__(self, magnitude=0.1, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.mode = magnitude, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        seq_len = o.shape[-1]
        lambd = np.random.beta(self.magnitude, self.magnitude)
        lambd = min(lambd, 1 - lambd)
        output = o.clone()[..., int(round(lambd * seq_len)):]
        return F.interpolate(output, size=seq_len, mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)

# Cell
class TSVarOut(RandTransform):
    "Set the value of a random number of variables to zero"
    order = 95
    def __init__(self, magnitude=0.05, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        in_vars = o.shape[-2]
        if in_vars == 1: return o
        lambd = np.random.beta(self.magnitude, self.magnitude)
        lambd = min(lambd, 1 - lambd)
        p = np.arange(in_vars).cumsum()
        p = p/p[-1]
        p = p / p.sum()
        p = p[::-1]
        out_vars = np.random.choice(np.arange(in_vars), int(round(lambd * in_vars)), p=p, replace=False)
        if len(out_vars) == 0:  return o
        output = o.clone()
        output[...,out_vars,:] = 0
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSCutOut(RandTransform):
    "Sets a random section of the sequence to zero"
    order = 95
    def __init__(self, magnitude=0.05, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        seq_len = o.shape[-1]
        lambd = np.random.beta(self.magnitude, self.magnitude)
        lambd = min(lambd, 1 - lambd)
        win_len = int(round(seq_len * lambd))
        start = np.random.randint(-win_len + 1, seq_len)
        end = start + win_len
        start = max(0, start)
        end = min(end, seq_len)
        output = o.clone()
        output[..., start:end] = 0
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSTimeStepOut(RandTransform):
    "Sets random sequence steps to zero"
    order = 95
    def __init__(self, magnitude=0.05, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        magnitude = min(.5, self.magnitude)
        seq_len = o.shape[-1]
        timesteps = np.sort(np.random.choice(np.arange(seq_len), int(round(seq_len * magnitude)), replace=False))
        output = o.clone()
        output[..., timesteps] = 0
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSRandomCropPad(RandTransform):
    "Crops a section of the sequence of a random length"
    order = 95
    def __init__(self, magnitude=0.05, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        seq_len = o.shape[-1]
        lambd = np.random.beta(self.magnitude, self.magnitude)
        lambd = max(lambd, 1 - lambd)
        win_len = int(round(seq_len * lambd))
        if win_len == seq_len: return o
        start = np.random.randint(0, seq_len - win_len)
        output = torch.zeros_like(o, dtype=o.dtype, device=o.device)
        output[..., start : start + win_len] = o[..., start : start + win_len]
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSMaskOut(RandTransform):
    "Set a random number of steps to zero"
    order = 95
    def __init__(self, magnitude=0.05, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        seq_len = o.shape[-1]
        mask = torch.rand_like(o) <= self.magnitude
        output = o.clone()
        output[mask] = 0
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSTranslateX(RandTransform):
    "Moves a selected sequence window a random number of steps"
    order = 90
    def __init__(self, magnitude=0.1, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        seq_len = o.shape[-1]
        lambd = np.random.beta(self.magnitude, self.magnitude)
        lambd = min(lambd, 1 - lambd)
        shift = int(round(seq_len * lambd))
        if shift == 0 or shift == seq_len: return o
        if np.random.rand() < 0.5: shift = -shift
        new_start = max(0, shift)
        new_end = min(seq_len + shift, seq_len)
        start = max(0, -shift)
        end = min(seq_len - shift, seq_len)
        output = torch.zeros_like(o, dtype=o.dtype, device=o.device)
        output[..., new_start : new_end] = o[..., start : end]
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSRandomShift(RandTransform):
    "Shifts and splits a sequence"
    order = 90
    def __init__(self, magnitude=0.02, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        pos = int(round(np.random.randint(0, o.shape[-1]) * self.magnitude)) * (random.randint(0, 1)*2-1)
        output = torch.cat((o[..., pos:], o[..., :pos]), dim=-1)
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSHorizontalFlip(RandTransform):
    "Flips the sequence along the x-axis"
    order = 90
    def __init__(self, magnitude=1., ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        output = torch.flip(o, [-1])
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSRandomTrend(RandTransform):
    "Randomly rotates the sequence along the z-axis"
    order = 90
    def __init__(self, magnitude=0.1, ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        flat_x = o.reshape(o.shape[0], -1)
        ran = flat_x.max(dim=-1, keepdim=True).values - flat_x.min(dim=-1, keepdim=True).values
        trend = torch.linspace(0, 1, o.shape[-1], device=o.device) * ran
        t = (1 + self.magnitude * 2 * (np.random.rand() - 0.5) * trend)
        t -= t.mean(-1, keepdim=True)
        if o.ndim == 3: t = t.unsqueeze(1)
        output = o + t
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

TSRandomRotate = TSRandomTrend

# Cell
class TSVerticalFlip(RandTransform):
    "Applies a negative value to the time sequence"
    order = 90
    def __init__(self, magnitude=1., ex=None, **kwargs):
        self.magnitude, self.ex = magnitude, ex
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        return - o

# Cell
class TSResize(RandTransform):
    "Resizes the sequence length of a time series"
    order = 80
    def __init__(self, magnitude=-0.5, size=None, ex=None, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.size, self.ex, self.mode = magnitude, size, ex, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if self.magnitude == 0: return o
        size = ifnone(self.size, int(round((1 + self.magnitude) * o.shape[-1])))
        output = F.interpolate(o, size=size, mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)
        return output

# Cell
class TSRandomSize(RandTransform):
    "Randomly resizes the sequence length of a time series"
    order = 80
    def __init__(self, magnitude=0., ex=None, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.ex, self.mode = magnitude, ex, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        size_perc = 1 / (1 + (random_half_normal() if random.random() > 1/3 else - random_half_normal() / 2) * (1 + self.magnitude))
        if random.random() > .5: size_perc = 1. / size_perc
        return F.interpolate(o, size=int(size_perc * o.shape[-1]), mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)

# Cell
class TSRandomLowRes(RandTransform):
    "Randomly resizes the sequence length of a time series to a lower resolution"
    order = 80
    def __init__(self, magnitude=.5, ex=None, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.ex, self.mode = magnitude, ex, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        size_perc = 1 - (np.random.rand() * (1 - self.magnitude))
        return F.interpolate(o, size=int(size_perc * o.shape[-1]), mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)

# Cell
class TSDownUpScale(RandTransform):
    "Downscales a time series and upscales it again to previous sequence length"
    order = 80
    def __init__(self, magnitude=0.5, ex=None, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.ex, self.mode = magnitude, ex, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0 or self.magnitude >= 1: return o
        output = F.interpolate(o, size=int((1 - self.magnitude) * o.shape[-1]), mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)
        output = F.interpolate(output, size=o.shape[-1], mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
class TSRandomDownUpScale(RandTransform):
    "Randomly downscales a time series and upscales it again to previous sequence length"
    order = 80
    def __init__(self, magnitude=.5, ex=None, mode='linear', **kwargs):
        "mode:  'nearest' | 'linear' | 'area'"
        self.magnitude, self.ex, self.mode = magnitude, ex, mode
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0 or self.magnitude >= 1: return o
        scale_factor = 0.5 + 0.5 * np.random.rand()
        output = F.interpolate(o, size=int(scale_factor * o.shape[-1]), mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)
        output = F.interpolate(output, size=o.shape[-1], mode=self.mode, align_corners=None if self.mode in ['nearest', 'area'] else False)
        if self.ex is not None: output[...,self.ex,:] = o[...,self.ex,:]
        return output

# Cell
all_TS_randaugs = [

    TSIdentity,

    # Noise
    (TSMagAddNoise, 0.1, 1.),
    (partial(TSMagMulNoise, ex=0), 0.1, 1),
    (partial(TSTimeNoise, ex=0), 0.1, 1.),
    (partial(TSRandomFreqNoise, ex=0), 0.1, 1.),
    partial(TSShuffleSteps, ex=0),
    (TSRandomTimeScale, 0.05, 0.5),
    (TSRandomTimeStep, 0.05, 0.5),
    (partial(TSFreqDenoise, ex=0), 0.1, 1.),
    (TSRandomLowRes, 0.05, 0.5),

    # Magnitude
    (partial(TSMagWarp, ex=0), 0.02, 0.2),
    (TSMagScale, 0.2, 1.),
    (partial(TSMagScalePerVar, ex=0), 0.2, 1.),
    partial(TSBlur, ex=0),
    partial(TSSmooth, ex=0),
    partial(TSDownUpScale, ex=0),
    partial(TSRandomDownUpScale, ex=0),
    (TSRandomTrend, 0.1, 0.5),
    TSVerticalFlip,
    (TSVarOut, 0.05, 0.5),
    (TSCutOut, 0.05, 0.5),

    # Time
    (partial(TSTimeWarp, ex=0), 0.02, 0.2),
    (TSWindowWarp, 0.05, 0.5),
    (TSRandomSize, 0.05, 1.),
    TSHorizontalFlip,
    (TSTranslateX, 0.1, 0.5),
    (TSRandomShift, 0.02, 0.2),
    (TSRandomZoomIn, 0.05, 0.5),
    (TSWindowSlicing, 0.05, 0.2),
    (TSRandomZoomOut, 0.05, 0.5),
    (TSRandomResizedLookBack, 0.1, 1.),
    (TSTimeStepOut, 0.01, 0.2),
    (TSRandomCropPad, 0.05, 0.5),
    (TSRandomResizedCrop, 0.05, 0.5),
    (TSMaskOut, 0.01, 0.2),
]

# Cell
class RandAugment(RandTransform):
    order = 60
    def __init__(self, tfms:list, N:int=1, M:int=3, **kwargs):
        '''
        tfms   : list of tfm functions (not called)
        N      : number of tfms applied to each batch (usual values 1-3)
        M      : tfm magnitude multiplier (1-10, usually 3-5). Only works if tfms are tuples (tfm, min, max)
        kwargs : RandTransform kwargs
        '''
        super().__init__(**kwargs)
        if not isinstance(tfms, list): tfms = [tfms]
        self.tfms, self.N, self.magnitude = tfms, min(len(tfms), N), M / 10
        self.n_tfms, self.tfms_idxs = len(tfms), np.arange(len(tfms))

    def encodes(self, o:(NumpyTensor, TSTensor)):
        if not self.N or not self.magnitude: return o
        tfms = self.tfms if self.n_tfms==1 else L(self.tfms)[np.random.choice(np.arange(self.n_tfms), self.N, replace=False)]
        tfms_ = []
        for tfm in tfms:
            if isinstance(tfm, tuple):
                t, min_val, max_val = tfm
                tfms_ += [t(magnitude=self.magnitude * float(max_val - min_val) + min_val)]
            else:  tfms_ += [tfm()]
        output = compose_tfms(o, tfms_, split_idx=self.split_idx)
        return output

# Cell
class TestTfm(RandTransform):
    "Utility class to test the output of selected tfms during training"
    def __init__(self, tfm, magnitude=1., ex=None, **kwargs):
        self.tfm, self.magnitude, self.ex = tfm, magnitude, ex
        self.tfmd, self.shape = [], []
        super().__init__(**kwargs)
    def encodes(self, o: (NumpyTensor, TSTensor)):
        if not self.magnitude or self.magnitude <= 0: return o
        output = self.tfm(o, split_idx=self.split_idx)
        self.tfmd.append(torch.equal(o, output))
        self.shape.append(o.shape)
        return output

# Cell
def get_tfm_name(tfm):
    if isinstance(tfm, tuple): tfm = tfm[0]
    if hasattr(tfm, "func"): tfm = tfm.func
    if hasattr(tfm, "__name__"): return tfm.__name__
    elif hasattr(tfm, "__class__") and hasattr(tfm.__class__, "__name__"): return tfm.__class__.__name__
    else: return tfm