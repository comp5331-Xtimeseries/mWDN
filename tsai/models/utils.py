# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/100_models.utils.ipynb (unless otherwise specified).

__all__ = ['get_layers', 'is_layer', 'is_linear', 'is_bn', 'is_conv_linear', 'is_affine_layer', 'is_conv', 'has_bias',
           'has_weight', 'has_weight_or_bias', 'check_bias', 'check_weight', 'create_model', 'create_tabular_model',
           'count_parameters', 'get_clones', 'get_nf', 'split_model', 'seq_len_calculator']

# Cell
from ..imports import *

# Cell
from fastai.tabular.model import *

# Cell
def get_layers(model, cond=noop):
    if isinstance(model, Learner): model=model.model
    return [m for m in flatten_model(model) if any([c(m) for c in L(cond)])]

def is_layer(*args):
    def _is_layer(l, cond=args):
        return isinstance(l, cond)
    return partial(_is_layer, cond=args)

def is_linear(l):
    return isinstance(l, nn.Linear)

def is_bn(l):
    types = (nn.BatchNorm1d, nn.BatchNorm2d, nn.BatchNorm3d)
    return isinstance(l, types)

def is_conv_linear(l):
    types = (nn.Conv1d, nn.Conv2d, nn.Conv3d, nn.Linear)
    return isinstance(l, types)

def is_affine_layer(l):
    return has_bias(l) or has_weight(l)

def is_conv(l):
    types = (nn.Conv1d, nn.Conv2d, nn.Conv3d)
    return isinstance(l, types)

def has_bias(l):
    return (hasattr(l, 'bias') and l.bias is not None)

def has_weight(l):
    return (hasattr(l, 'weight'))

def has_weight_or_bias(l):
    return any((has_weight(l), has_bias(l)))

# Cell
def check_bias(m, cond=noop, verbose=False):
    mean, std = [], []
    for i,l in enumerate(get_layers(m, cond=cond)):
        if hasattr(l, 'bias') and l.bias is not None:
            b = l.bias.data
            mean.append(b.mean())
            std.append(b.std())
            pv(f'{i:3} {l.__class__.__name__:15} shape: {str(list(b.shape)):15}  mean: {b.mean():+6.3f}  std: {b.std():+6.3f}', verbose)
    return np.array(mean), np.array(std)

def check_weight(m, cond=noop, verbose=False):
    mean, std = [], []
    for i,l in enumerate(get_layers(m, cond=cond)):
        if hasattr(l, 'weight') and l.weight is not None:
            w = l.weight.data
            mean.append(w.mean())
            std.append(w.std())
            pv(f'{i:3} {l.__class__.__name__:15} shape: {str(list(w.shape)):15}  mean: {w.mean():+6.3f}  std: {w.std():+6.3f}', verbose)
    return np.array(mean), np.array(std)

# Cell
def create_model(arch, c_in=1, c_out=2, seq_len=32, dls=None, device=default_device(), **kwargs):
    if dls is not None: c_in, c_out, seq_len = dls.vars, dls.c, dls.len
    if sum([1 for v in ['RNN_FCN', 'LSTM_FCN', 'RNNPlus', 'LSTMPlus', 'GRUPlus', 'InceptionTimePlus', 'GRU_FCN', 'OmniScaleCNN', 'mWDN', 'TST']
            if v in arch.__name__]):
        return arch(c_in, c_out, seq_len=seq_len, **kwargs).to(device=device)
    elif 'xresnet' in arch.__name__ and not '1d' in arch.__name__:
        return (arch(c_in=c_in, n_out=c_out, **kwargs)).to(device=device)
    elif 'rocket' in arch.__name__.lower():
        return (arch(c_in=c_in, seq_len=seq_len, **kwargs)).to(device=device)
    else:
        return arch(c_in, c_out, **kwargs).to(device=device)


@delegates(TabularModel.__init__)
def create_tabular_model(arch, dls, layers=None, emb_szs=None, n_out=None, y_range=None, device=None, **kwargs):
    if device is None: device = default_device()
    if layers is None: layers = [200,100]
    emb_szs = get_emb_sz(dls.train_ds, {} if emb_szs is None else emb_szs)
    if n_out is None: n_out = get_c(dls)
    assert n_out, "`n_out` is not defined, and could not be inferred from data, set `dls.c` or pass `n_out`"
    if y_range is None and 'y_range' in kwargs: y_range = kwargs.pop('y_range')
    return arch(emb_szs, len(dls.cont_names), n_out, layers, y_range=y_range, **kwargs).to(device=device)


def count_parameters(model, trainable=True):
    if trainable: return sum(p.numel() for p in model.parameters() if p.requires_grad)
    else: return sum(p.numel() for p in model.parameters())

# Cell
def get_clones(module, N):
    return nn.ModuleList([deepcopy(module) for i in range(N)])

# Cell
def get_nf(m):
    "Get nf from model's last linear layer"
    if hasattr(m, 'head_nf'): return m.head_nf
    return get_layers(m, cond=is_linear)[-1].in_features

# Cell
def split_model(model):
    if hasattr(model, "head"): head = model.head
    else:
        print('This model cannot be split as a head attribute is not available')
        return
    model.head = Identity()
    body = model
    return body, head

# Cell
def seq_len_calculator(seq_len, **kwargs):
    t = torch.rand(1, 1, seq_len)
    return nn.Conv1d(1, 1, **kwargs)(t).shape[-1]