# Trained models

The save are generated from the following commands:

<details> 
<summary> 
(this is a template )[save name]

```command``` 
</summary>
<p>
  
```
console output
```
</details> 

<details> 
<summary> 
exchange_rate.pt
  
```python main.py --gpu 0 --data exchange_rate --save exchange_rate.pt --hidCNN 50 --hidRNN 50 --L1Loss False --output_fun None``` 
</summary>
<p>
  
```
tensor(0.4558)
* number of parameters: 19998
/usr/local/lib/python3.6/dist-packages/torch/nn/_reduction.py:44: UserWarning: size_average and reduce args will be deprecated, please use reduction='sum' instead.
  warnings.warn(warning.format(ret))
begin training
| end of epoch   1 | time:  0.51s | train_loss 0.1227 | valid rse 0.1829 | valid rae 0.1809 | valid corr  0.7909
| end of epoch   2 | time:  0.46s | train_loss 0.0363 | valid rse 0.0785 | valid rae 0.0658 | valid corr  0.9134
| end of epoch   3 | time:  0.44s | train_loss 0.0216 | valid rse 0.0706 | valid rae 0.0606 | valid corr  0.9488
| end of epoch   4 | time:  0.44s | train_loss 0.0185 | valid rse 0.0851 | valid rae 0.0690 | valid corr  0.9490
| end of epoch   5 | time:  0.45s | train_loss 0.0170 | valid rse 0.0810 | valid rae 0.0638 | valid corr  0.9511
test rse 0.0764 | test rae 0.0618 | test corr 0.9457
| end of epoch   6 | time:  0.47s | train_loss 0.0162 | valid rse 0.0676 | valid rae 0.0589 | valid corr  0.9520
| end of epoch   7 | time:  0.46s | train_loss 0.0143 | valid rse 0.0683 | valid rae 0.0544 | valid corr  0.9527
| end of epoch   8 | time:  0.45s | train_loss 0.0134 | valid rse 0.0630 | valid rae 0.0514 | valid corr  0.9533
| end of epoch   9 | time:  0.44s | train_loss 0.0131 | valid rse 0.0632 | valid rae 0.0508 | valid corr  0.9537
| end of epoch  10 | time:  0.46s | train_loss 0.0125 | valid rse 0.0623 | valid rae 0.0498 | valid corr  0.9541
test rse 0.0401 | test rae 0.0332 | test corr 0.9492
| end of epoch  11 | time:  0.44s | train_loss 0.0123 | valid rse 0.0616 | valid rae 0.0488 | valid corr  0.9546
| end of epoch  12 | time:  0.45s | train_loss 0.0123 | valid rse 0.0646 | valid rae 0.0511 | valid corr  0.9551
| end of epoch  13 | time:  0.45s | train_loss 0.0124 | valid rse 0.0648 | valid rae 0.0513 | valid corr  0.9556
| end of epoch  14 | time:  0.44s | train_loss 0.0119 | valid rse 0.0665 | valid rae 0.0525 | valid corr  0.9561
| end of epoch  15 | time:  0.46s | train_loss 0.0121 | valid rse 0.0620 | valid rae 0.0488 | valid corr  0.9565
test rse 0.0424 | test rae 0.0355 | test corr 0.9503
| end of epoch  16 | time:  0.44s | train_loss 0.0117 | valid rse 0.0593 | valid rae 0.0474 | valid corr  0.9565
| end of epoch  17 | time:  0.48s | train_loss 0.0117 | valid rse 0.0642 | valid rae 0.0571 | valid corr  0.9574
| end of epoch  18 | time:  0.45s | train_loss 0.0135 | valid rse 0.0606 | valid rae 0.0480 | valid corr  0.9574
| end of epoch  19 | time:  0.45s | train_loss 0.0124 | valid rse 0.0610 | valid rae 0.0481 | valid corr  0.9573
| end of epoch  20 | time:  0.50s | train_loss 0.0113 | valid rse 0.0593 | valid rae 0.0468 | valid corr  0.9578
test rse 0.0390 | test rae 0.0325 | test corr 0.9511
| end of epoch  21 | time:  0.46s | train_loss 0.0112 | valid rse 0.0595 | valid rae 0.0469 | valid corr  0.9587
| end of epoch  22 | time:  0.44s | train_loss 0.0117 | valid rse 0.0584 | valid rae 0.0470 | valid corr  0.9587
| end of epoch  23 | time:  0.51s | train_loss 0.0115 | valid rse 0.0595 | valid rae 0.0480 | valid corr  0.9591
| end of epoch  24 | time:  0.44s | train_loss 0.0115 | valid rse 0.0588 | valid rae 0.0470 | valid corr  0.9593
| end of epoch  25 | time:  0.44s | train_loss 0.0114 | valid rse 0.0575 | valid rae 0.0460 | valid corr  0.9598
test rse 0.0385 | test rae 0.0322 | test corr 0.9524
| end of epoch  26 | time:  0.45s | train_loss 0.0113 | valid rse 0.0611 | valid rae 0.0540 | valid corr  0.9598
| end of epoch  27 | time:  0.44s | train_loss 0.0115 | valid rse 0.0578 | valid rae 0.0471 | valid corr  0.9595
| end of epoch  28 | time:  0.47s | train_loss 0.0112 | valid rse 0.0607 | valid rae 0.0481 | valid corr  0.9603
| end of epoch  29 | time:  0.48s | train_loss 0.0112 | valid rse 0.0578 | valid rae 0.0456 | valid corr  0.9608
| end of epoch  30 | time:  0.46s | train_loss 0.0108 | valid rse 0.0566 | valid rae 0.0468 | valid corr  0.9601
test rse 0.0387 | test rae 0.0332 | test corr 0.9509
| end of epoch  31 | time:  0.45s | train_loss 0.0108 | valid rse 0.0571 | valid rae 0.0471 | valid corr  0.9604
| end of epoch  32 | time:  0.45s | train_loss 0.0108 | valid rse 0.0573 | valid rae 0.0452 | valid corr  0.9610
| end of epoch  33 | time:  0.44s | train_loss 0.0107 | valid rse 0.0587 | valid rae 0.0462 | valid corr  0.9613
| end of epoch  34 | time:  0.44s | train_loss 0.0112 | valid rse 0.0567 | valid rae 0.0455 | valid corr  0.9610
| end of epoch  35 | time:  0.44s | train_loss 0.0108 | valid rse 0.0581 | valid rae 0.0458 | valid corr  0.9612
test rse 0.0392 | test rae 0.0327 | test corr 0.9530
| end of epoch  36 | time:  0.44s | train_loss 0.0109 | valid rse 0.0577 | valid rae 0.0457 | valid corr  0.9614
| end of epoch  37 | time:  0.44s | train_loss 0.0108 | valid rse 0.0580 | valid rae 0.0467 | valid corr  0.9609
| end of epoch  38 | time:  0.44s | train_loss 0.0107 | valid rse 0.0568 | valid rae 0.0454 | valid corr  0.9620
| end of epoch  39 | time:  0.45s | train_loss 0.0106 | valid rse 0.0558 | valid rae 0.0455 | valid corr  0.9625
| end of epoch  40 | time:  0.44s | train_loss 0.0109 | valid rse 0.0545 | valid rae 0.0446 | valid corr  0.9626
test rse 0.0382 | test rae 0.0317 | test corr 0.9532
| end of epoch  41 | time:  0.47s | train_loss 0.0107 | valid rse 0.0584 | valid rae 0.0462 | valid corr  0.9626
| end of epoch  42 | time:  0.47s | train_loss 0.0109 | valid rse 0.0558 | valid rae 0.0440 | valid corr  0.9625
| end of epoch  43 | time:  0.44s | train_loss 0.0106 | valid rse 0.0591 | valid rae 0.0467 | valid corr  0.9626
| end of epoch  44 | time:  0.44s | train_loss 0.0106 | valid rse 0.0547 | valid rae 0.0453 | valid corr  0.9627
| end of epoch  45 | time:  0.45s | train_loss 0.0106 | valid rse 0.0561 | valid rae 0.0476 | valid corr  0.9630
test rse 0.0408 | test rae 0.0345 | test corr 0.9531
| end of epoch  46 | time:  0.49s | train_loss 0.0108 | valid rse 0.0636 | valid rae 0.0511 | valid corr  0.9629
| end of epoch  47 | time:  0.44s | train_loss 0.0113 | valid rse 0.0553 | valid rae 0.0443 | valid corr  0.9629
| end of epoch  48 | time:  0.45s | train_loss 0.0105 | valid rse 0.0582 | valid rae 0.0457 | valid corr  0.9631
| end of epoch  49 | time:  0.44s | train_loss 0.0105 | valid rse 0.0551 | valid rae 0.0438 | valid corr  0.9632
| end of epoch  50 | time:  0.45s | train_loss 0.0103 | valid rse 0.0544 | valid rae 0.0439 | valid corr  0.9634
test rse 0.0364 | test rae 0.0300 | test corr 0.9535
| end of epoch  51 | time:  0.44s | train_loss 0.0112 | valid rse 0.0548 | valid rae 0.0438 | valid corr  0.9634
| end of epoch  52 | time:  0.51s | train_loss 0.0107 | valid rse 0.0539 | valid rae 0.0435 | valid corr  0.9635
| end of epoch  53 | time:  0.45s | train_loss 0.0104 | valid rse 0.0559 | valid rae 0.0442 | valid corr  0.9636
| end of epoch  54 | time:  0.48s | train_loss 0.0103 | valid rse 0.0535 | valid rae 0.0436 | valid corr  0.9634
| end of epoch  55 | time:  0.46s | train_loss 0.0105 | valid rse 0.0544 | valid rae 0.0447 | valid corr  0.9635
test rse 0.0368 | test rae 0.0307 | test corr 0.9534
| end of epoch  56 | time:  0.48s | train_loss 0.0104 | valid rse 0.0555 | valid rae 0.0480 | valid corr  0.9635
| end of epoch  57 | time:  0.46s | train_loss 0.0104 | valid rse 0.0563 | valid rae 0.0445 | valid corr  0.9638
| end of epoch  58 | time:  0.47s | train_loss 0.0104 | valid rse 0.0556 | valid rae 0.0445 | valid corr  0.9636
| end of epoch  59 | time:  0.54s | train_loss 0.0105 | valid rse 0.0569 | valid rae 0.0448 | valid corr  0.9638
| end of epoch  60 | time:  0.51s | train_loss 0.0106 | valid rse 0.0536 | valid rae 0.0447 | valid corr  0.9638
test rse 0.0373 | test rae 0.0313 | test corr 0.9534
| end of epoch  61 | time:  0.44s | train_loss 0.0107 | valid rse 0.0564 | valid rae 0.0499 | valid corr  0.9640
| end of epoch  62 | time:  0.45s | train_loss 0.0108 | valid rse 0.0539 | valid rae 0.0438 | valid corr  0.9639
| end of epoch  63 | time:  0.44s | train_loss 0.0104 | valid rse 0.0560 | valid rae 0.0444 | valid corr  0.9639
| end of epoch  64 | time:  0.44s | train_loss 0.0103 | valid rse 0.0538 | valid rae 0.0454 | valid corr  0.9641
| end of epoch  65 | time:  0.45s | train_loss 0.0102 | valid rse 0.0565 | valid rae 0.0460 | valid corr  0.9635
test rse 0.0386 | test rae 0.0318 | test corr 0.9536
| end of epoch  66 | time:  0.49s | train_loss 0.0108 | valid rse 0.0533 | valid rae 0.0430 | valid corr  0.9642
| end of epoch  67 | time:  0.53s | train_loss 0.0102 | valid rse 0.0534 | valid rae 0.0428 | valid corr  0.9641
| end of epoch  68 | time:  0.54s | train_loss 0.0102 | valid rse 0.0534 | valid rae 0.0454 | valid corr  0.9643
| end of epoch  69 | time:  0.49s | train_loss 0.0102 | valid rse 0.0538 | valid rae 0.0435 | valid corr  0.9644
| end of epoch  70 | time:  0.44s | train_loss 0.0104 | valid rse 0.0561 | valid rae 0.0497 | valid corr  0.9639
test rse 0.0394 | test rae 0.0347 | test corr 0.9534
| end of epoch  71 | time:  0.44s | train_loss 0.0103 | valid rse 0.0546 | valid rae 0.0432 | valid corr  0.9645
| end of epoch  72 | time:  0.47s | train_loss 0.0104 | valid rse 0.0550 | valid rae 0.0478 | valid corr  0.9638
| end of epoch  73 | time:  0.46s | train_loss 0.0117 | valid rse 0.0527 | valid rae 0.0430 | valid corr  0.9638
| end of epoch  74 | time:  0.49s | train_loss 0.0104 | valid rse 0.0548 | valid rae 0.0438 | valid corr  0.9644
| end of epoch  75 | time:  0.56s | train_loss 0.0102 | valid rse 0.0611 | valid rae 0.0493 | valid corr  0.9646
test rse 0.0453 | test rae 0.0393 | test corr 0.9537
| end of epoch  76 | time:  0.54s | train_loss 0.0104 | valid rse 0.0549 | valid rae 0.0438 | valid corr  0.9644
| end of epoch  77 | time:  0.50s | train_loss 0.0102 | valid rse 0.0559 | valid rae 0.0444 | valid corr  0.9642
| end of epoch  78 | time:  0.46s | train_loss 0.0103 | valid rse 0.0580 | valid rae 0.0467 | valid corr  0.9647
| end of epoch  79 | time:  0.45s | train_loss 0.0104 | valid rse 0.0531 | valid rae 0.0426 | valid corr  0.9638
| end of epoch  80 | time:  0.46s | train_loss 0.0103 | valid rse 0.0529 | valid rae 0.0444 | valid corr  0.9645
test rse 0.0362 | test rae 0.0302 | test corr 0.9535
| end of epoch  81 | time:  0.45s | train_loss 0.0103 | valid rse 0.0564 | valid rae 0.0448 | valid corr  0.9645
| end of epoch  82 | time:  0.45s | train_loss 0.0103 | valid rse 0.0531 | valid rae 0.0433 | valid corr  0.9646
| end of epoch  83 | time:  0.46s | train_loss 0.0100 | valid rse 0.0527 | valid rae 0.0436 | valid corr  0.9646
| end of epoch  84 | time:  0.45s | train_loss 0.0100 | valid rse 0.0538 | valid rae 0.0429 | valid corr  0.9643
| end of epoch  85 | time:  0.46s | train_loss 0.0104 | valid rse 0.0536 | valid rae 0.0427 | valid corr  0.9646
test rse 0.0376 | test rae 0.0308 | test corr 0.9534
| end of epoch  86 | time:  0.46s | train_loss 0.0101 | valid rse 0.0526 | valid rae 0.0425 | valid corr  0.9647
| end of epoch  87 | time:  0.45s | train_loss 0.0104 | valid rse 0.0525 | valid rae 0.0425 | valid corr  0.9640
| end of epoch  88 | time:  0.46s | train_loss 0.0102 | valid rse 0.0544 | valid rae 0.0433 | valid corr  0.9647
| end of epoch  89 | time:  0.45s | train_loss 0.0099 | valid rse 0.0526 | valid rae 0.0429 | valid corr  0.9648
| end of epoch  90 | time:  0.45s | train_loss 0.0103 | valid rse 0.0527 | valid rae 0.0444 | valid corr  0.9650
test rse 0.0365 | test rae 0.0306 | test corr 0.9529
| end of epoch  91 | time:  0.46s | train_loss 0.0100 | valid rse 0.0543 | valid rae 0.0433 | valid corr  0.9648
| end of epoch  92 | time:  0.45s | train_loss 0.0104 | valid rse 0.0520 | valid rae 0.0423 | valid corr  0.9649
| end of epoch  93 | time:  0.48s | train_loss 0.0101 | valid rse 0.0538 | valid rae 0.0430 | valid corr  0.9649
| end of epoch  94 | time:  0.56s | train_loss 0.0102 | valid rse 0.0537 | valid rae 0.0433 | valid corr  0.9646
| end of epoch  95 | time:  0.55s | train_loss 0.0103 | valid rse 0.0527 | valid rae 0.0429 | valid corr  0.9648
test rse 0.0361 | test rae 0.0298 | test corr 0.9536
| end of epoch  96 | time:  0.45s | train_loss 0.0102 | valid rse 0.0546 | valid rae 0.0476 | valid corr  0.9648
| end of epoch  97 | time:  0.44s | train_loss 0.0113 | valid rse 0.0535 | valid rae 0.0456 | valid corr  0.9648
| end of epoch  98 | time:  0.45s | train_loss 0.0100 | valid rse 0.0547 | valid rae 0.0439 | valid corr  0.9650
| end of epoch  99 | time:  0.44s | train_loss 0.0100 | valid rse 0.0538 | valid rae 0.0467 | valid corr  0.9648
| end of epoch 100 | time:  0.45s | train_loss 0.0099 | valid rse 0.0531 | valid rae 0.0430 | valid corr  0.9649
test rse 0.0366 | test rae 0.0300 | test corr 0.9536
test rse 0.0357 | test rae 0.0296 | test corr 0.9538
```
</p>
</details>

<details> 
<summary> 
elec.pt

```python main.py --gpu 0 --horizon 24 --data electricity --save elec.pt --output_fun Linear``` 
</summary>
<p>
  
```
tcmalloc: large alloc 3363168256 bytes == 0x12dce000 @  0x7fdb7e07cb6b 0x7fdb7e09c379 0x7fdb3278992e 0x7fdb3278b946 0x7fdb6a67c9e5 0x7fdb6a901af3 0x7fdb6a8f2f97 0x7fdb6a8f2c7d 0x7fdb6a8f2f97 0x7fdb6a9fda1a 0x7fdb6a6750c5 0x7fdb6aa942f3 0x7fdb6a8f3319 0x7fdb6a8ee5ff 0x7fdb6a8f3319 0x7fdb6a9e8fb5 0x7fdb7a06074b 0x50a4a5 0x50beb4 0x5095c8 0x50a2fd 0x50beb4 0x5095c8 0x50a2fd 0x50beb4 0x507be4 0x508f37 0x594a01 0x549e8f 0x5515c1 0x5a9dac
tensor(16619.3613)
* number of parameters: 325871
/usr/local/lib/python3.6/dist-packages/torch/nn/_reduction.py:44: UserWarning: size_average and reduce args will be deprecated, please use reduction='sum' instead.
  warnings.warn(warning.format(ret))
begin training
main.py:45: RuntimeWarning: invalid value encountered in true_divide
  correlation = ((predict - mean_p) * (Ytest - mean_g)).mean(axis = 0)/(sigma_p * sigma_g);
| end of epoch   1 | time:  4.37s | train_loss 1101.4482 | valid rse 0.1222 | valid rae 0.1018 | valid corr  0.6720
| end of epoch   2 | time:  4.21s | train_loss 418.2790 | valid rse 0.1189 | valid rae 0.0849 | valid corr  0.8111
| end of epoch   3 | time:  4.28s | train_loss 314.5622 | valid rse 0.0902 | valid rae 0.0663 | valid corr  0.8371
| end of epoch   4 | time:  4.23s | train_loss 264.5292 | valid rse 0.0872 | valid rae 0.0624 | valid corr  0.8492
| end of epoch   5 | time:  4.18s | train_loss 240.0109 | valid rse 0.0781 | valid rae 0.0575 | valid corr  0.8597
test rse 0.1207 | test rae 0.0689 | test corr 0.8697
| end of epoch   6 | time:  4.23s | train_loss 229.4223 | valid rse 0.0734 | valid rae 0.0550 | valid corr  0.8648
| end of epoch   7 | time:  4.26s | train_loss 217.8766 | valid rse 0.0801 | valid rae 0.0557 | valid corr  0.8704
| end of epoch   8 | time:  4.22s | train_loss 211.8440 | valid rse 0.0721 | valid rae 0.0520 | valid corr  0.8758
| end of epoch   9 | time:  4.23s | train_loss 204.4028 | valid rse 0.0714 | valid rae 0.0531 | valid corr  0.8740
| end of epoch  10 | time:  4.28s | train_loss 200.3260 | valid rse 0.0712 | valid rae 0.0510 | valid corr  0.8866
test rse 0.1054 | test rae 0.0610 | test corr 0.8940
| end of epoch  11 | time:  4.19s | train_loss 201.4333 | valid rse 0.0709 | valid rae 0.0507 | valid corr  0.8796
| end of epoch  12 | time:  4.26s | train_loss 198.6667 | valid rse 0.0682 | valid rae 0.0507 | valid corr  0.8714
| end of epoch  13 | time:  4.27s | train_loss 194.5647 | valid rse 0.0685 | valid rae 0.0485 | valid corr  0.8870
| end of epoch  14 | time:  4.26s | train_loss 191.4807 | valid rse 0.0713 | valid rae 0.0502 | valid corr  0.8913
| end of epoch  15 | time:  4.31s | train_loss 189.5628 | valid rse 0.0680 | valid rae 0.0477 | valid corr  0.8899
test rse 0.1017 | test rae 0.0574 | test corr 0.8989
| end of epoch  16 | time:  4.29s | train_loss 187.0239 | valid rse 0.0664 | valid rae 0.0473 | valid corr  0.8899
| end of epoch  17 | time:  4.26s | train_loss 187.4547 | valid rse 0.0666 | valid rae 0.0471 | valid corr  0.8926
| end of epoch  18 | time:  4.25s | train_loss 184.4588 | valid rse 0.0655 | valid rae 0.0465 | valid corr  0.8923
| end of epoch  19 | time:  4.21s | train_loss 185.2956 | valid rse 0.0651 | valid rae 0.0463 | valid corr  0.8916
| end of epoch  20 | time:  4.23s | train_loss 182.9515 | valid rse 0.0668 | valid rae 0.0478 | valid corr  0.8939
test rse 0.1009 | test rae 0.0577 | test corr 0.9023
| end of epoch  21 | time:  4.16s | train_loss 182.1376 | valid rse 0.0650 | valid rae 0.0460 | valid corr  0.8934
| end of epoch  22 | time:  4.21s | train_loss 181.0200 | valid rse 0.0674 | valid rae 0.0464 | valid corr  0.8956
| end of epoch  23 | time:  4.18s | train_loss 181.4476 | valid rse 0.0647 | valid rae 0.0467 | valid corr  0.8946
| end of epoch  24 | time:  4.19s | train_loss 180.3809 | valid rse 0.0667 | valid rae 0.0461 | valid corr  0.8950
| end of epoch  25 | time:  4.21s | train_loss 182.1215 | valid rse 0.0671 | valid rae 0.0462 | valid corr  0.8938
test rse 0.1049 | test rae 0.0571 | test corr 0.9024
| end of epoch  26 | time:  4.15s | train_loss 182.2695 | valid rse 0.0659 | valid rae 0.0467 | valid corr  0.8914
| end of epoch  27 | time:  4.17s | train_loss 182.7902 | valid rse 0.0648 | valid rae 0.0450 | valid corr  0.8931
| end of epoch  28 | time:  4.25s | train_loss 180.8101 | valid rse 0.0647 | valid rae 0.0448 | valid corr  0.8945
| end of epoch  29 | time:  4.19s | train_loss 181.5435 | valid rse 0.0650 | valid rae 0.0452 | valid corr  0.8941
| end of epoch  30 | time:  4.13s | train_loss 179.6669 | valid rse 0.0648 | valid rae 0.0451 | valid corr  0.8927
test rse 0.1014 | test rae 0.0560 | test corr 0.8999
| end of epoch  31 | time:  4.23s | train_loss 179.8732 | valid rse 0.0658 | valid rae 0.0453 | valid corr  0.8950
| end of epoch  32 | time:  4.21s | train_loss 179.6422 | valid rse 0.0648 | valid rae 0.0448 | valid corr  0.8946
| end of epoch  33 | time:  4.13s | train_loss 178.6589 | valid rse 0.0648 | valid rae 0.0445 | valid corr  0.8952
| end of epoch  34 | time:  4.28s | train_loss 178.2668 | valid rse 0.0667 | valid rae 0.0457 | valid corr  0.8942
| end of epoch  35 | time:  4.13s | train_loss 180.1492 | valid rse 0.0648 | valid rae 0.0450 | valid corr  0.8948
test rse 0.0992 | test rae 0.0553 | test corr 0.9024
| end of epoch  36 | time:  4.22s | train_loss 179.7984 | valid rse 0.0643 | valid rae 0.0444 | valid corr  0.8940
| end of epoch  37 | time:  4.23s | train_loss 177.8986 | valid rse 0.0660 | valid rae 0.0459 | valid corr  0.8943
| end of epoch  38 | time:  4.22s | train_loss 177.7318 | valid rse 0.0652 | valid rae 0.0450 | valid corr  0.8947
| end of epoch  39 | time:  4.15s | train_loss 178.9835 | valid rse 0.0644 | valid rae 0.0453 | valid corr  0.8947
| end of epoch  40 | time:  4.12s | train_loss 178.5640 | valid rse 0.0650 | valid rae 0.0462 | valid corr  0.8914
test rse 0.0992 | test rae 0.0577 | test corr 0.8974
| end of epoch  41 | time:  4.26s | train_loss 177.4263 | valid rse 0.0658 | valid rae 0.0470 | valid corr  0.8914
| end of epoch  42 | time:  4.22s | train_loss 177.3309 | valid rse 0.0649 | valid rae 0.0462 | valid corr  0.8969
| end of epoch  43 | time:  4.16s | train_loss 177.5521 | valid rse 0.0650 | valid rae 0.0457 | valid corr  0.8956
| end of epoch  44 | time:  4.14s | train_loss 177.1846 | valid rse 0.0643 | valid rae 0.0444 | valid corr  0.8959
| end of epoch  45 | time:  4.23s | train_loss 177.4881 | valid rse 0.0644 | valid rae 0.0448 | valid corr  0.8961
test rse 0.1025 | test rae 0.0554 | test corr 0.9036
| end of epoch  46 | time:  4.18s | train_loss 177.1668 | valid rse 0.0651 | valid rae 0.0449 | valid corr  0.8959
| end of epoch  47 | time:  4.11s | train_loss 176.3696 | valid rse 0.0663 | valid rae 0.0457 | valid corr  0.8954
| end of epoch  48 | time:  4.22s | train_loss 176.7119 | valid rse 0.0672 | valid rae 0.0464 | valid corr  0.8954
| end of epoch  49 | time:  4.20s | train_loss 178.3391 | valid rse 0.0671 | valid rae 0.0489 | valid corr  0.8939
| end of epoch  50 | time:  4.22s | train_loss 176.9720 | valid rse 0.0654 | valid rae 0.0458 | valid corr  0.8960
test rse 0.0992 | test rae 0.0556 | test corr 0.9042
| end of epoch  51 | time:  4.20s | train_loss 176.4478 | valid rse 0.0649 | valid rae 0.0448 | valid corr  0.8965
| end of epoch  52 | time:  4.24s | train_loss 177.0063 | valid rse 0.0642 | valid rae 0.0452 | valid corr  0.8950
| end of epoch  53 | time:  4.21s | train_loss 176.9040 | valid rse 0.0634 | valid rae 0.0444 | valid corr  0.8966
| end of epoch  54 | time:  4.12s | train_loss 174.5991 | valid rse 0.0657 | valid rae 0.0452 | valid corr  0.8983
| end of epoch  55 | time:  4.22s | train_loss 175.7961 | valid rse 0.0647 | valid rae 0.0450 | valid corr  0.8966
test rse 0.0990 | test rae 0.0552 | test corr 0.9043
| end of epoch  56 | time:  4.18s | train_loss 174.9223 | valid rse 0.0631 | valid rae 0.0438 | valid corr  0.8973
| end of epoch  57 | time:  4.21s | train_loss 175.7264 | valid rse 0.0637 | valid rae 0.0445 | valid corr  0.8977
| end of epoch  58 | time:  4.15s | train_loss 175.2912 | valid rse 0.0643 | valid rae 0.0444 | valid corr  0.8981
| end of epoch  59 | time:  4.19s | train_loss 175.0858 | valid rse 0.0651 | valid rae 0.0446 | valid corr  0.8970
| end of epoch  60 | time:  4.11s | train_loss 174.4565 | valid rse 0.0653 | valid rae 0.0450 | valid corr  0.8958
test rse 0.1079 | test rae 0.0567 | test corr 0.9017
| end of epoch  61 | time:  4.24s | train_loss 177.5405 | valid rse 0.0655 | valid rae 0.0453 | valid corr  0.8952
| end of epoch  62 | time:  4.13s | train_loss 175.5859 | valid rse 0.0648 | valid rae 0.0451 | valid corr  0.8955
| end of epoch  63 | time:  4.18s | train_loss 176.1795 | valid rse 0.0646 | valid rae 0.0451 | valid corr  0.8966
| end of epoch  64 | time:  4.25s | train_loss 176.3229 | valid rse 0.0651 | valid rae 0.0454 | valid corr  0.8962
| end of epoch  65 | time:  4.24s | train_loss 180.1917 | valid rse 0.0655 | valid rae 0.0447 | valid corr  0.8963
test rse 0.1018 | test rae 0.0552 | test corr 0.9041
| end of epoch  66 | time:  4.17s | train_loss 179.3205 | valid rse 0.0656 | valid rae 0.0451 | valid corr  0.8942
| end of epoch  67 | time:  4.15s | train_loss 178.2019 | valid rse 0.0660 | valid rae 0.0450 | valid corr  0.8929
| end of epoch  68 | time:  4.24s | train_loss 180.0595 | valid rse 0.0664 | valid rae 0.0454 | valid corr  0.8938
| end of epoch  69 | time:  4.18s | train_loss 178.0562 | valid rse 0.0656 | valid rae 0.0450 | valid corr  0.8950
| end of epoch  70 | time:  4.16s | train_loss 178.1484 | valid rse 0.0666 | valid rae 0.0460 | valid corr  0.8934
test rse 0.1008 | test rae 0.0572 | test corr 0.8974
| end of epoch  71 | time:  4.25s | train_loss 181.2769 | valid rse 0.0643 | valid rae 0.0442 | valid corr  0.8962
| end of epoch  72 | time:  4.20s | train_loss 177.4542 | valid rse 0.0653 | valid rae 0.0448 | valid corr  0.8945
| end of epoch  73 | time:  4.21s | train_loss 176.9958 | valid rse 0.0649 | valid rae 0.0446 | valid corr  0.8938
| end of epoch  74 | time:  4.20s | train_loss 177.2610 | valid rse 0.0656 | valid rae 0.0453 | valid corr  0.8958
| end of epoch  75 | time:  4.18s | train_loss 177.3724 | valid rse 0.0661 | valid rae 0.0450 | valid corr  0.8907
test rse 0.1030 | test rae 0.0553 | test corr 0.9011
| end of epoch  76 | time:  4.22s | train_loss 177.3994 | valid rse 0.0650 | valid rae 0.0443 | valid corr  0.8972
| end of epoch  77 | time:  4.18s | train_loss 180.0074 | valid rse 0.0649 | valid rae 0.0446 | valid corr  0.8980
| end of epoch  78 | time:  4.17s | train_loss 177.0120 | valid rse 0.0648 | valid rae 0.0443 | valid corr  0.8978
| end of epoch  79 | time:  4.18s | train_loss 176.1667 | valid rse 0.0645 | valid rae 0.0441 | valid corr  0.8986
| end of epoch  80 | time:  4.21s | train_loss 175.1882 | valid rse 0.0651 | valid rae 0.0445 | valid corr  0.8961
test rse 0.1005 | test rae 0.0556 | test corr 0.8997
| end of epoch  81 | time:  4.23s | train_loss 175.7518 | valid rse 0.0639 | valid rae 0.0437 | valid corr  0.8986
| end of epoch  82 | time:  4.16s | train_loss 176.2375 | valid rse 0.0652 | valid rae 0.0445 | valid corr  0.8944
| end of epoch  83 | time:  4.20s | train_loss 177.4929 | valid rse 0.0657 | valid rae 0.0457 | valid corr  0.8968
| end of epoch  84 | time:  4.15s | train_loss 176.8157 | valid rse 0.0651 | valid rae 0.0446 | valid corr  0.8963
| end of epoch  85 | time:  4.16s | train_loss 176.1301 | valid rse 0.0673 | valid rae 0.0477 | valid corr  0.8897
test rse 0.1029 | test rae 0.0601 | test corr 0.8914
| end of epoch  86 | time:  4.22s | train_loss 178.1202 | valid rse 0.0643 | valid rae 0.0439 | valid corr  0.8968
| end of epoch  87 | time:  4.17s | train_loss 175.3880 | valid rse 0.0646 | valid rae 0.0440 | valid corr  0.8987
| end of epoch  88 | time:  4.20s | train_loss 177.0220 | valid rse 0.0647 | valid rae 0.0440 | valid corr  0.8985
| end of epoch  89 | time:  4.23s | train_loss 175.9814 | valid rse 0.0643 | valid rae 0.0439 | valid corr  0.8996
| end of epoch  90 | time:  4.18s | train_loss 174.3806 | valid rse 0.0644 | valid rae 0.0439 | valid corr  0.8998
test rse 0.1030 | test rae 0.0552 | test corr 0.9046
| end of epoch  91 | time:  4.20s | train_loss 174.2926 | valid rse 0.0650 | valid rae 0.0442 | valid corr  0.9005
| end of epoch  92 | time:  4.17s | train_loss 173.9383 | valid rse 0.0649 | valid rae 0.0445 | valid corr  0.8977
| end of epoch  93 | time:  4.10s | train_loss 175.3273 | valid rse 0.0640 | valid rae 0.0437 | valid corr  0.8993
| end of epoch  94 | time:  4.26s | train_loss 174.5309 | valid rse 0.0645 | valid rae 0.0441 | valid corr  0.8983
| end of epoch  95 | time:  4.13s | train_loss 173.6329 | valid rse 0.0643 | valid rae 0.0439 | valid corr  0.8993
test rse 0.1005 | test rae 0.0550 | test corr 0.9032
| end of epoch  96 | time:  4.24s | train_loss 174.0393 | valid rse 0.0637 | valid rae 0.0440 | valid corr  0.8996
| end of epoch  97 | time:  4.16s | train_loss 173.7447 | valid rse 0.0641 | valid rae 0.0444 | valid corr  0.8998
| end of epoch  98 | time:  4.21s | train_loss 176.5816 | valid rse 0.0644 | valid rae 0.0440 | valid corr  0.9004
| end of epoch  99 | time:  4.20s | train_loss 173.5798 | valid rse 0.0650 | valid rae 0.0445 | valid corr  0.9002
| end of epoch 100 | time:  4.19s | train_loss 172.4303 | valid rse 0.0641 | valid rae 0.0436 | valid corr  0.9012
test rse 0.1011 | test rae 0.0550 | test corr 0.9031
test rse 0.0995 | test rae 0.0542 | test corr 0.9049
```
</p>
</details>

<details> 
<summary> 
solar_AL.pt

```python main.py --data solar --save solar_AL.pt --hidSkip 10 --output_fun Linear --cuda True --gpu 0``` 
</summary>
<p>
  
```
tensor(8.9212)
* number of parameters: 193002
/usr/local/lib/python3.6/dist-packages/torch/nn/_reduction.py:44: UserWarning: size_average and reduce args will be deprecated, please use reduction='sum' instead.
  warnings.warn(warning.format(ret))
begin training
| end of epoch   1 | time: 35.60s | train_loss 2.9826 | valid rse 0.4546 | valid rae 0.3138 | valid corr  0.9191
| end of epoch   2 | time: 36.81s | train_loss 2.1557 | valid rse 0.4609 | valid rae 0.3017 | valid corr  0.9242
| end of epoch   3 | time: 36.54s | train_loss 2.0129 | valid rse 0.4305 | valid rae 0.2794 | valid corr  0.9280
| end of epoch   4 | time: 36.59s | train_loss 1.8842 | valid rse 0.4284 | valid rae 0.2734 | valid corr  0.9290
| end of epoch   5 | time: 36.64s | train_loss 1.8269 | valid rse 0.4338 | valid rae 0.2768 | valid corr  0.9287
test rse 0.4324 | test rae 0.2423 | test corr 0.9104
| end of epoch   6 | time: 36.60s | train_loss 1.7772 | valid rse 0.4360 | valid rae 0.2845 | valid corr  0.9268
| end of epoch   7 | time: 36.60s | train_loss 1.7571 | valid rse 0.4236 | valid rae 0.2603 | valid corr  0.9310
| end of epoch   8 | time: 36.56s | train_loss 1.7277 | valid rse 0.4218 | valid rae 0.2602 | valid corr  0.9316
| end of epoch   9 | time: 36.58s | train_loss 1.7042 | valid rse 0.4351 | valid rae 0.2645 | valid corr  0.9303
| end of epoch  10 | time: 36.57s | train_loss 1.6970 | valid rse 0.4471 | valid rae 0.2774 | valid corr  0.9306
test rse 0.4484 | test rae 0.2544 | test corr 0.9069
| end of epoch  11 | time: 36.68s | train_loss 1.6783 | valid rse 0.4229 | valid rae 0.2607 | valid corr  0.9312
| end of epoch  12 | time: 36.65s | train_loss 1.6587 | valid rse 0.4237 | valid rae 0.2583 | valid corr  0.9314
| end of epoch  13 | time: 36.58s | train_loss 1.6414 | valid rse 0.4257 | valid rae 0.2585 | valid corr  0.9307
| end of epoch  14 | time: 36.60s | train_loss 1.6273 | valid rse 0.4246 | valid rae 0.2643 | valid corr  0.9305
| end of epoch  15 | time: 36.56s | train_loss 1.6195 | valid rse 0.4276 | valid rae 0.2599 | valid corr  0.9307
test rse 0.4370 | test rae 0.2389 | test corr 0.9058
| end of epoch  16 | time: 36.55s | train_loss 1.6199 | valid rse 0.4247 | valid rae 0.2603 | valid corr  0.9309
| end of epoch  17 | time: 36.58s | train_loss 1.6067 | valid rse 0.4272 | valid rae 0.2585 | valid corr  0.9308
| end of epoch  18 | time: 36.53s | train_loss 1.5991 | valid rse 0.4282 | valid rae 0.2600 | valid corr  0.9301
| end of epoch  19 | time: 36.62s | train_loss 1.5965 | valid rse 0.4250 | valid rae 0.2596 | valid corr  0.9301
| end of epoch  20 | time: 36.58s | train_loss 1.5913 | valid rse 0.4431 | valid rae 0.2682 | valid corr  0.9293
test rse 0.4447 | test rae 0.2457 | test corr 0.9026
| end of epoch  21 | time: 36.56s | train_loss 1.5914 | valid rse 0.4248 | valid rae 0.2583 | valid corr  0.9302
| end of epoch  22 | time: 36.56s | train_loss 1.5868 | valid rse 0.4229 | valid rae 0.2619 | valid corr  0.9298
| end of epoch  23 | time: 36.54s | train_loss 1.5776 | valid rse 0.4263 | valid rae 0.2635 | valid corr  0.9288
| end of epoch  24 | time: 36.63s | train_loss 1.5648 | valid rse 0.4276 | valid rae 0.2683 | valid corr  0.9287
| end of epoch  25 | time: 36.53s | train_loss 1.5616 | valid rse 0.4307 | valid rae 0.2593 | valid corr  0.9293
test rse 0.4414 | test rae 0.2460 | test corr 0.9025
| end of epoch  26 | time: 36.62s | train_loss 1.5551 | valid rse 0.4279 | valid rae 0.2685 | valid corr  0.9289
| end of epoch  27 | time: 36.58s | train_loss 1.5504 | valid rse 0.4300 | valid rae 0.2671 | valid corr  0.9279
| end of epoch  28 | time: 36.59s | train_loss 1.5498 | valid rse 0.4290 | valid rae 0.2624 | valid corr  0.9288
| end of epoch  29 | time: 36.57s | train_loss 1.5477 | valid rse 0.4300 | valid rae 0.2681 | valid corr  0.9283
| end of epoch  30 | time: 36.56s | train_loss 1.5449 | valid rse 0.4322 | valid rae 0.2640 | valid corr  0.9274
test rse 0.4455 | test rae 0.2527 | test corr 0.9008
| end of epoch  31 | time: 36.64s | train_loss 1.5350 | valid rse 0.4329 | valid rae 0.2615 | valid corr  0.9273
| end of epoch  32 | time: 36.53s | train_loss 1.5464 | valid rse 0.4483 | valid rae 0.2751 | valid corr  0.9254
| end of epoch  33 | time: 36.55s | train_loss 1.5379 | valid rse 0.4437 | valid rae 0.2696 | valid corr  0.9257
| end of epoch  34 | time: 36.59s | train_loss 1.5274 | valid rse 0.4327 | valid rae 0.2671 | valid corr  0.9266
| end of epoch  35 | time: 36.59s | train_loss 1.5189 | valid rse 0.4463 | valid rae 0.2748 | valid corr  0.9254
test rse 0.4579 | test rae 0.2595 | test corr 0.8966
| end of epoch  36 | time: 36.65s | train_loss 1.5215 | valid rse 0.4369 | valid rae 0.2676 | valid corr  0.9257
| end of epoch  37 | time: 36.55s | train_loss 1.5346 | valid rse 0.4390 | valid rae 0.2653 | valid corr  0.9261
| end of epoch  38 | time: 36.61s | train_loss 1.5201 | valid rse 0.4321 | valid rae 0.2654 | valid corr  0.9266
| end of epoch  39 | time: 36.60s | train_loss 1.5239 | valid rse 0.4372 | valid rae 0.2649 | valid corr  0.9269
| end of epoch  40 | time: 36.57s | train_loss 1.5050 | valid rse 0.4406 | valid rae 0.2688 | valid corr  0.9266
test rse 0.4530 | test rae 0.2546 | test corr 0.8974
| end of epoch  41 | time: 36.60s | train_loss 1.5071 | valid rse 0.4375 | valid rae 0.2663 | valid corr  0.9267
| end of epoch  42 | time: 36.60s | train_loss 1.5000 | valid rse 0.4436 | valid rae 0.2680 | valid corr  0.9269
| end of epoch  43 | time: 36.58s | train_loss 1.4963 | valid rse 0.4395 | valid rae 0.2645 | valid corr  0.9262
| end of epoch  44 | time: 36.66s | train_loss 1.4932 | valid rse 0.4462 | valid rae 0.2732 | valid corr  0.9239
| end of epoch  45 | time: 36.54s | train_loss 1.4964 | valid rse 0.4359 | valid rae 0.2690 | valid corr  0.9249
test rse 0.4607 | test rae 0.2690 | test corr 0.8927
| end of epoch  46 | time: 36.58s | train_loss 1.4941 | valid rse 0.4435 | valid rae 0.2674 | valid corr  0.9262
| end of epoch  47 | time: 36.59s | train_loss 1.4936 | valid rse 0.4469 | valid rae 0.2692 | valid corr  0.9249
| end of epoch  48 | time: 36.58s | train_loss 1.4807 | valid rse 0.4444 | valid rae 0.2700 | valid corr  0.9250
| end of epoch  49 | time: 36.64s | train_loss 1.4786 | valid rse 0.4487 | valid rae 0.2757 | valid corr  0.9239
| end of epoch  50 | time: 36.55s | train_loss 1.4790 | valid rse 0.4474 | valid rae 0.2721 | valid corr  0.9241
test rse 0.4589 | test rae 0.2587 | test corr 0.8938
| end of epoch  51 | time: 36.59s | train_loss 1.4861 | valid rse 0.4487 | valid rae 0.2707 | valid corr  0.9241
| end of epoch  52 | time: 36.55s | train_loss 1.4789 | valid rse 0.4453 | valid rae 0.2739 | valid corr  0.9223
| end of epoch  53 | time: 36.55s | train_loss 1.4763 | valid rse 0.4539 | valid rae 0.2741 | valid corr  0.9249
| end of epoch  54 | time: 36.61s | train_loss 1.4666 | valid rse 0.4493 | valid rae 0.2732 | valid corr  0.9234
| end of epoch  55 | time: 36.58s | train_loss 1.4742 | valid rse 0.4599 | valid rae 0.2801 | valid corr  0.9234
test rse 0.4623 | test rae 0.2582 | test corr 0.8922
| end of epoch  56 | time: 36.61s | train_loss 1.4616 | valid rse 0.4477 | valid rae 0.2691 | valid corr  0.9248
| end of epoch  57 | time: 36.59s | train_loss 1.4606 | valid rse 0.4603 | valid rae 0.2778 | valid corr  0.9247
| end of epoch  58 | time: 36.57s | train_loss 1.4559 | valid rse 0.4487 | valid rae 0.2737 | valid corr  0.9241
| end of epoch  59 | time: 36.57s | train_loss 1.4575 | valid rse 0.4523 | valid rae 0.2744 | valid corr  0.9221
| end of epoch  60 | time: 36.52s | train_loss 1.4550 | valid rse 0.4451 | valid rae 0.2679 | valid corr  0.9245
test rse 0.4610 | test rae 0.2586 | test corr 0.8917
| end of epoch  61 | time: 36.56s | train_loss 1.4482 | valid rse 0.4552 | valid rae 0.2757 | valid corr  0.9233
| end of epoch  62 | time: 36.53s | train_loss 1.4489 | valid rse 0.4494 | valid rae 0.2721 | valid corr  0.9236
| end of epoch  63 | time: 36.54s | train_loss 1.4475 | valid rse 0.4414 | valid rae 0.2679 | valid corr  0.9249
| end of epoch  64 | time: 36.57s | train_loss 1.4458 | valid rse 0.4493 | valid rae 0.2728 | valid corr  0.9242
| end of epoch  65 | time: 36.56s | train_loss 1.4591 | valid rse 0.4556 | valid rae 0.2773 | valid corr  0.9219
test rse 0.4719 | test rae 0.2674 | test corr 0.8866
| end of epoch  66 | time: 36.59s | train_loss 1.4471 | valid rse 0.4453 | valid rae 0.2693 | valid corr  0.9241
| end of epoch  67 | time: 36.51s | train_loss 1.4398 | valid rse 0.4578 | valid rae 0.2761 | valid corr  0.9232
| end of epoch  68 | time: 36.51s | train_loss 1.4555 | valid rse 0.4557 | valid rae 0.2760 | valid corr  0.9228
| end of epoch  69 | time: 36.47s | train_loss 1.4399 | valid rse 0.4545 | valid rae 0.2772 | valid corr  0.9212
| end of epoch  70 | time: 36.57s | train_loss 1.4443 | valid rse 0.4526 | valid rae 0.2731 | valid corr  0.9239
test rse 0.4713 | test rae 0.2652 | test corr 0.8879
| end of epoch  71 | time: 36.61s | train_loss 1.4381 | valid rse 0.4507 | valid rae 0.2749 | valid corr  0.9230
| end of epoch  72 | time: 36.54s | train_loss 1.4290 | valid rse 0.4514 | valid rae 0.2750 | valid corr  0.9230
| end of epoch  73 | time: 36.50s | train_loss 1.4463 | valid rse 0.4619 | valid rae 0.2799 | valid corr  0.9206
| end of epoch  74 | time: 36.53s | train_loss 1.4429 | valid rse 0.4566 | valid rae 0.2779 | valid corr  0.9230
| end of epoch  75 | time: 36.56s | train_loss 1.4234 | valid rse 0.4465 | valid rae 0.2714 | valid corr  0.9236
test rse 0.4730 | test rae 0.2712 | test corr 0.8858
| end of epoch  76 | time: 36.69s | train_loss 1.4417 | valid rse 0.4532 | valid rae 0.2821 | valid corr  0.9216
| end of epoch  77 | time: 36.57s | train_loss 1.4282 | valid rse 0.4571 | valid rae 0.2778 | valid corr  0.9241
| end of epoch  78 | time: 36.58s | train_loss 1.4167 | valid rse 0.4456 | valid rae 0.2699 | valid corr  0.9235
| end of epoch  79 | time: 36.51s | train_loss 1.4308 | valid rse 0.4538 | valid rae 0.2781 | valid corr  0.9228
| end of epoch  80 | time: 36.46s | train_loss 1.4194 | valid rse 0.4603 | valid rae 0.2818 | valid corr  0.9200
test rse 0.4809 | test rae 0.2752 | test corr 0.8831
| end of epoch  81 | time: 36.56s | train_loss 1.4278 | valid rse 0.4583 | valid rae 0.2763 | valid corr  0.9219
| end of epoch  82 | time: 36.54s | train_loss 1.4395 | valid rse 0.4478 | valid rae 0.2756 | valid corr  0.9228
| end of epoch  83 | time: 36.52s | train_loss 1.4189 | valid rse 0.4460 | valid rae 0.2728 | valid corr  0.9238
| end of epoch  84 | time: 36.78s | train_loss 1.4240 | valid rse 0.4561 | valid rae 0.2762 | valid corr  0.9222
| end of epoch  85 | time: 36.76s | train_loss 1.4040 | valid rse 0.4740 | valid rae 0.2883 | valid corr  0.9221
test rse 0.4838 | test rae 0.2787 | test corr 0.8863
| end of epoch  86 | time: 36.66s | train_loss 1.4161 | valid rse 0.4498 | valid rae 0.2717 | valid corr  0.9241
| end of epoch  87 | time: 36.56s | train_loss 1.4064 | valid rse 0.4560 | valid rae 0.2768 | valid corr  0.9244
| end of epoch  88 | time: 36.54s | train_loss 1.4146 | valid rse 0.4547 | valid rae 0.2790 | valid corr  0.9231
| end of epoch  89 | time: 36.70s | train_loss 1.4183 | valid rse 0.4444 | valid rae 0.2717 | valid corr  0.9248
| end of epoch  90 | time: 36.71s | train_loss 1.4189 | valid rse 0.4509 | valid rae 0.2763 | valid corr  0.9243
test rse 0.4708 | test rae 0.2787 | test corr 0.8879
| end of epoch  91 | time: 36.64s | train_loss 1.4007 | valid rse 0.4406 | valid rae 0.2724 | valid corr  0.9248
| end of epoch  92 | time: 36.59s | train_loss 1.4022 | valid rse 0.4459 | valid rae 0.2787 | valid corr  0.9242
| end of epoch  93 | time: 36.60s | train_loss 1.3918 | valid rse 0.4421 | valid rae 0.2721 | valid corr  0.9277
| end of epoch  94 | time: 36.61s | train_loss 1.3945 | valid rse 0.4386 | valid rae 0.2778 | valid corr  0.9306
| end of epoch  95 | time: 36.55s | train_loss 1.3906 | valid rse 0.4286 | valid rae 0.2748 | valid corr  0.9322
test rse 0.4343 | test rae 0.2855 | test corr 0.9035
| end of epoch  96 | time: 36.55s | train_loss 1.3854 | valid rse 0.4252 | valid rae 0.2653 | valid corr  0.9319
| end of epoch  97 | time: 36.50s | train_loss 1.3736 | valid rse 0.4209 | valid rae 0.2677 | valid corr  0.9336
| end of epoch  98 | time: 36.52s | train_loss 1.3703 | valid rse 0.4155 | valid rae 0.2657 | valid corr  0.9373
| end of epoch  99 | time: 36.57s | train_loss 1.3527 | valid rse 0.4162 | valid rae 0.2644 | valid corr  0.9381
| end of epoch 100 | time: 36.55s | train_loss 1.3301 | valid rse 0.4165 | valid rae 0.2667 | valid corr  0.9386
test rse 0.4316 | test rae 0.2853 | test corr 0.9068
test rse 0.4239 | test rae 0.2844 | test corr 0.9094
```
</p>
</details>

<details> 
<summary> 
traffic.pt

```python main.py --gpu 0 --data traffic --save traffic.pt --hidSkip 10``` 
</summary>
<p>
  
```
tensor(0.0571)
* number of parameters: 875227
/usr/local/lib/python3.6/dist-packages/torch/nn/_reduction.py:43: UserWarning: size_average and reduce args will be deprecated, please use reduction='sum' instead.
  warnings.warn(warning.format(ret))
begin training
/usr/local/lib/python3.6/dist-packages/torch/nn/functional.py:1350: UserWarning: nn.functional.sigmoid is deprecated. Use torch.sigmoid instead.
  warnings.warn("nn.functional.sigmoid is deprecated. Use torch.sigmoid instead.")
| end of epoch   1 | time:  9.51s | train_loss 0.0336 | valid rse 0.6509 | valid rae 0.4940 | valid corr  0.7787
| end of epoch   2 | time:  9.42s | train_loss 0.0166 | valid rse 0.5499 | valid rae 0.3920 | valid corr  0.8216
| end of epoch   3 | time:  9.49s | train_loss 0.0146 | valid rse 0.5204 | valid rae 0.3676 | valid corr  0.8423
| end of epoch   4 | time:  9.51s | train_loss 0.0136 | valid rse 0.5305 | valid rae 0.3814 | valid corr  0.8464
| end of epoch   5 | time:  9.49s | train_loss 0.0127 | valid rse 0.4908 | valid rae 0.3377 | valid corr  0.8581
test rse 0.5377 | test rae 0.3852 | test corr 0.8417
| end of epoch   6 | time:  9.58s | train_loss 0.0122 | valid rse 0.4832 | valid rae 0.3328 | valid corr  0.8601
| end of epoch   7 | time:  9.72s | train_loss 0.0116 | valid rse 0.4805 | valid rae 0.3300 | valid corr  0.8635
| end of epoch   8 | time:  9.44s | train_loss 0.0116 | valid rse 0.4824 | valid rae 0.3264 | valid corr  0.8633
| end of epoch   9 | time:  9.53s | train_loss 0.0112 | valid rse 0.5104 | valid rae 0.3577 | valid corr  0.8606
| end of epoch  10 | time:  9.55s | train_loss 0.0111 | valid rse 0.4770 | valid rae 0.3118 | valid corr  0.8676
test rse 0.5219 | test rae 0.3608 | test corr 0.8516
| end of epoch  11 | time:  9.70s | train_loss 0.0108 | valid rse 0.4727 | valid rae 0.3119 | valid corr  0.8680
| end of epoch  12 | time:  9.63s | train_loss 0.0107 | valid rse 0.4782 | valid rae 0.3201 | valid corr  0.8689
| end of epoch  13 | time:  9.62s | train_loss 0.0106 | valid rse 0.4731 | valid rae 0.3125 | valid corr  0.8679
| end of epoch  14 | time:  9.61s | train_loss 0.0105 | valid rse 0.4681 | valid rae 0.3073 | valid corr  0.8704
| end of epoch  15 | time:  9.50s | train_loss 0.0104 | valid rse 0.4710 | valid rae 0.3119 | valid corr  0.8716
test rse 0.5239 | test rae 0.3644 | test corr 0.8506
| end of epoch  16 | time:  9.57s | train_loss 0.0103 | valid rse 0.4749 | valid rae 0.3155 | valid corr  0.8704
| end of epoch  17 | time:  9.58s | train_loss 0.0103 | valid rse 0.4745 | valid rae 0.3181 | valid corr  0.8733
| end of epoch  18 | time:  9.54s | train_loss 0.0102 | valid rse 0.4913 | valid rae 0.3350 | valid corr  0.8695
| end of epoch  19 | time:  9.46s | train_loss 0.0101 | valid rse 0.4903 | valid rae 0.3314 | valid corr  0.8692
| end of epoch  20 | time:  9.60s | train_loss 0.0101 | valid rse 0.4691 | valid rae 0.3117 | valid corr  0.8734
test rse 0.5185 | test rae 0.3597 | test corr 0.8561
| end of epoch  21 | time:  9.48s | train_loss 0.0101 | valid rse 0.4609 | valid rae 0.2998 | valid corr  0.8737
| end of epoch  22 | time:  9.56s | train_loss 0.0099 | valid rse 0.4664 | valid rae 0.3024 | valid corr  0.8747
| end of epoch  23 | time:  9.49s | train_loss 0.0098 | valid rse 0.4654 | valid rae 0.3038 | valid corr  0.8736
| end of epoch  24 | time:  9.71s | train_loss 0.0098 | valid rse 0.4676 | valid rae 0.3044 | valid corr  0.8735
| end of epoch  25 | time:  9.59s | train_loss 0.0097 | valid rse 0.4602 | valid rae 0.2969 | valid corr  0.8763
test rse 0.5114 | test rae 0.3516 | test corr 0.8582
| end of epoch  26 | time:  9.52s | train_loss 0.0097 | valid rse 0.4623 | valid rae 0.2998 | valid corr  0.8747
| end of epoch  27 | time:  9.56s | train_loss 0.0097 | valid rse 0.4607 | valid rae 0.2969 | valid corr  0.8760
| end of epoch  28 | time:  9.73s | train_loss 0.0096 | valid rse 0.4674 | valid rae 0.3059 | valid corr  0.8744
| end of epoch  29 | time:  9.63s | train_loss 0.0096 | valid rse 0.4634 | valid rae 0.3033 | valid corr  0.8734
| end of epoch  30 | time:  9.63s | train_loss 0.0095 | valid rse 0.4658 | valid rae 0.3033 | valid corr  0.8740
test rse 0.5070 | test rae 0.3461 | test corr 0.8627
| end of epoch  31 | time:  9.51s | train_loss 0.0095 | valid rse 0.4607 | valid rae 0.3030 | valid corr  0.8754
| end of epoch  32 | time:  9.54s | train_loss 0.0095 | valid rse 0.4597 | valid rae 0.2975 | valid corr  0.8755
| end of epoch  33 | time:  9.48s | train_loss 0.0094 | valid rse 0.4621 | valid rae 0.2995 | valid corr  0.8768
| end of epoch  34 | time:  9.50s | train_loss 0.0094 | valid rse 0.4706 | valid rae 0.3076 | valid corr  0.8728
| end of epoch  35 | time:  9.51s | train_loss 0.0093 | valid rse 0.4610 | valid rae 0.2962 | valid corr  0.8768
test rse 0.5114 | test rae 0.3492 | test corr 0.8597
| end of epoch  36 | time:  9.78s | train_loss 0.0093 | valid rse 0.4639 | valid rae 0.3022 | valid corr  0.8758
| end of epoch  37 | time:  9.57s | train_loss 0.0093 | valid rse 0.4581 | valid rae 0.2939 | valid corr  0.8776
| end of epoch  38 | time:  9.69s | train_loss 0.0093 | valid rse 0.4649 | valid rae 0.3065 | valid corr  0.8765
| end of epoch  39 | time:  9.52s | train_loss 0.0092 | valid rse 0.4659 | valid rae 0.3067 | valid corr  0.8744
| end of epoch  40 | time:  9.60s | train_loss 0.0092 | valid rse 0.4577 | valid rae 0.2926 | valid corr  0.8763
test rse 0.5176 | test rae 0.3557 | test corr 0.8549
| end of epoch  41 | time:  9.44s | train_loss 0.0092 | valid rse 0.4647 | valid rae 0.3013 | valid corr  0.8746
| end of epoch  42 | time:  9.57s | train_loss 0.0091 | valid rse 0.4600 | valid rae 0.2969 | valid corr  0.8740
| end of epoch  43 | time:  9.42s | train_loss 0.0091 | valid rse 0.4575 | valid rae 0.2933 | valid corr  0.8760
| end of epoch  44 | time:  9.55s | train_loss 0.0091 | valid rse 0.4653 | valid rae 0.3016 | valid corr  0.8757
| end of epoch  45 | time:  9.60s | train_loss 0.0091 | valid rse 0.4604 | valid rae 0.2972 | valid corr  0.8767
test rse 0.5188 | test rae 0.3577 | test corr 0.8559
| end of epoch  46 | time:  9.56s | train_loss 0.0091 | valid rse 0.4615 | valid rae 0.2948 | valid corr  0.8756
| end of epoch  47 | time:  9.50s | train_loss 0.0090 | valid rse 0.4558 | valid rae 0.2929 | valid corr  0.8763
| end of epoch  48 | time:  9.52s | train_loss 0.0090 | valid rse 0.4691 | valid rae 0.3029 | valid corr  0.8741
| end of epoch  49 | time:  9.62s | train_loss 0.0090 | valid rse 0.4590 | valid rae 0.2967 | valid corr  0.8773
| end of epoch  50 | time:  9.60s | train_loss 0.0090 | valid rse 0.4621 | valid rae 0.3006 | valid corr  0.8761
test rse 0.5140 | test rae 0.3513 | test corr 0.8591
| end of epoch  51 | time:  9.50s | train_loss 0.0090 | valid rse 0.4550 | valid rae 0.2908 | valid corr  0.8766
| end of epoch  52 | time:  9.52s | train_loss 0.0090 | valid rse 0.4582 | valid rae 0.2944 | valid corr  0.8769
| end of epoch  53 | time:  9.57s | train_loss 0.0089 | valid rse 0.4578 | valid rae 0.2904 | valid corr  0.8757
| end of epoch  54 | time:  9.70s | train_loss 0.0089 | valid rse 0.4626 | valid rae 0.2971 | valid corr  0.8744
| end of epoch  55 | time:  9.56s | train_loss 0.0088 | valid rse 0.4591 | valid rae 0.2918 | valid corr  0.8764
test rse 0.5083 | test rae 0.3452 | test corr 0.8619
| end of epoch  56 | time:  9.62s | train_loss 0.0088 | valid rse 0.4588 | valid rae 0.2954 | valid corr  0.8773
| end of epoch  57 | time:  9.51s | train_loss 0.0088 | valid rse 0.4558 | valid rae 0.2883 | valid corr  0.8774
| end of epoch  58 | time:  9.55s | train_loss 0.0088 | valid rse 0.4551 | valid rae 0.2937 | valid corr  0.8775
| end of epoch  59 | time:  9.64s | train_loss 0.0088 | valid rse 0.4656 | valid rae 0.3010 | valid corr  0.8746
| end of epoch  60 | time:  9.55s | train_loss 0.0088 | valid rse 0.4599 | valid rae 0.2948 | valid corr  0.8753
test rse 0.5093 | test rae 0.3456 | test corr 0.8606
| end of epoch  61 | time:  9.72s | train_loss 0.0088 | valid rse 0.4553 | valid rae 0.2864 | valid corr  0.8761
| end of epoch  62 | time:  9.53s | train_loss 0.0087 | valid rse 0.4604 | valid rae 0.2940 | valid corr  0.8761
| end of epoch  63 | time:  9.50s | train_loss 0.0087 | valid rse 0.4521 | valid rae 0.2851 | valid corr  0.8777
| end of epoch  64 | time:  9.46s | train_loss 0.0087 | valid rse 0.4601 | valid rae 0.2952 | valid corr  0.8753
| end of epoch  65 | time:  9.53s | train_loss 0.0087 | valid rse 0.4526 | valid rae 0.2866 | valid corr  0.8779
test rse 0.5157 | test rae 0.3526 | test corr 0.8558
| end of epoch  66 | time:  9.55s | train_loss 0.0087 | valid rse 0.4580 | valid rae 0.2925 | valid corr  0.8753
| end of epoch  67 | time:  9.61s | train_loss 0.0086 | valid rse 0.4562 | valid rae 0.2885 | valid corr  0.8759
| end of epoch  68 | time:  9.82s | train_loss 0.0086 | valid rse 0.4542 | valid rae 0.2872 | valid corr  0.8772
| end of epoch  69 | time:  9.54s | train_loss 0.0086 | valid rse 0.4514 | valid rae 0.2847 | valid corr  0.8784
| end of epoch  70 | time:  9.52s | train_loss 0.0086 | valid rse 0.4612 | valid rae 0.2938 | valid corr  0.8755
test rse 0.5090 | test rae 0.3442 | test corr 0.8610
| end of epoch  71 | time:  9.71s | train_loss 0.0086 | valid rse 0.4561 | valid rae 0.2882 | valid corr  0.8762
| end of epoch  72 | time:  9.50s | train_loss 0.0086 | valid rse 0.4580 | valid rae 0.2914 | valid corr  0.8752
| end of epoch  73 | time:  9.54s | train_loss 0.0086 | valid rse 0.4529 | valid rae 0.2841 | valid corr  0.8770
| end of epoch  74 | time:  9.51s | train_loss 0.0085 | valid rse 0.4580 | valid rae 0.2913 | valid corr  0.8765
| end of epoch  75 | time:  9.49s | train_loss 0.0085 | valid rse 0.4551 | valid rae 0.2893 | valid corr  0.8763
test rse 0.5087 | test rae 0.3442 | test corr 0.8604
| end of epoch  76 | time:  9.60s | train_loss 0.0085 | valid rse 0.4556 | valid rae 0.2915 | valid corr  0.8767
| end of epoch  77 | time:  9.56s | train_loss 0.0085 | valid rse 0.4567 | valid rae 0.2904 | valid corr  0.8766
| end of epoch  78 | time:  9.68s | train_loss 0.0085 | valid rse 0.4556 | valid rae 0.2883 | valid corr  0.8761
| end of epoch  79 | time:  9.62s | train_loss 0.0085 | valid rse 0.4582 | valid rae 0.2957 | valid corr  0.8764
| end of epoch  80 | time:  9.63s | train_loss 0.0085 | valid rse 0.4537 | valid rae 0.2870 | valid corr  0.8782
test rse 0.5083 | test rae 0.3423 | test corr 0.8613
| end of epoch  81 | time:  9.46s | train_loss 0.0084 | valid rse 0.4575 | valid rae 0.2890 | valid corr  0.8752
| end of epoch  82 | time:  9.50s | train_loss 0.0085 | valid rse 0.4535 | valid rae 0.2842 | valid corr  0.8769
| end of epoch  83 | time:  9.59s | train_loss 0.0084 | valid rse 0.4583 | valid rae 0.2890 | valid corr  0.8754
| end of epoch  84 | time:  9.57s | train_loss 0.0084 | valid rse 0.4554 | valid rae 0.2860 | valid corr  0.8762
| end of epoch  85 | time:  9.63s | train_loss 0.0084 | valid rse 0.4557 | valid rae 0.2873 | valid corr  0.8769
test rse 0.5122 | test rae 0.3466 | test corr 0.8590
| end of epoch  86 | time:  9.43s | train_loss 0.0084 | valid rse 0.4544 | valid rae 0.2873 | valid corr  0.8769
| end of epoch  87 | time:  9.60s | train_loss 0.0084 | valid rse 0.4574 | valid rae 0.2891 | valid corr  0.8759
| end of epoch  88 | time:  9.57s | train_loss 0.0084 | valid rse 0.4596 | valid rae 0.2911 | valid corr  0.8741
| end of epoch  89 | time:  9.62s | train_loss 0.0084 | valid rse 0.4500 | valid rae 0.2800 | valid corr  0.8784
| end of epoch  90 | time:  9.60s | train_loss 0.0084 | valid rse 0.4570 | valid rae 0.2882 | valid corr  0.8756
test rse 0.5026 | test rae 0.3346 | test corr 0.8643
| end of epoch  91 | time:  9.76s | train_loss 0.0084 | valid rse 0.4551 | valid rae 0.2868 | valid corr  0.8758
| end of epoch  92 | time:  9.62s | train_loss 0.0084 | valid rse 0.4568 | valid rae 0.2890 | valid corr  0.8765
| end of epoch  93 | time:  9.49s | train_loss 0.0083 | valid rse 0.4546 | valid rae 0.2878 | valid corr  0.8769
| end of epoch  94 | time:  9.52s | train_loss 0.0084 | valid rse 0.4542 | valid rae 0.2857 | valid corr  0.8761
| end of epoch  95 | time:  9.55s | train_loss 0.0083 | valid rse 0.4563 | valid rae 0.2875 | valid corr  0.8758
test rse 0.5006 | test rae 0.3330 | test corr 0.8646
| end of epoch  96 | time:  9.64s | train_loss 0.0083 | valid rse 0.4582 | valid rae 0.2924 | valid corr  0.8754
| end of epoch  97 | time:  9.52s | train_loss 0.0083 | valid rse 0.4589 | valid rae 0.2899 | valid corr  0.8757
| end of epoch  98 | time:  9.66s | train_loss 0.0083 | valid rse 0.4536 | valid rae 0.2858 | valid corr  0.8762
| end of epoch  99 | time:  9.54s | train_loss 0.0083 | valid rse 0.4570 | valid rae 0.2885 | valid corr  0.8762
| end of epoch 100 | time:  9.48s | train_loss 0.0083 | valid rse 0.4505 | valid rae 0.2806 | valid corr  0.8781
test rse 0.5118 | test rae 0.3451 | test corr 0.8573
test rse 0.5071 | test rae 0.3404 | test corr 0.8598
```
</p>
</details>


<details> 
<summary> 
sp500.pt

```python main.py --gpu 0 --data sp500 --save sp500.pt --window 60 --horizon 6 --skip 20 --CNN_kernel 6 --hidSkip 1``` 
</summary>
<p>
  
```
tensor(124.3959)
2 20
* number of parameters: 399904
/usr/local/lib/python3.6/dist-packages/torch/nn/_reduction.py:43: UserWarning: size_average and reduce args will be deprecated, please use reduction='sum' instead.
  warnings.warn(warning.format(ret))
begin training
/usr/local/lib/python3.6/dist-packages/torch/nn/functional.py:1350: UserWarning: nn.functional.sigmoid is deprecated. Use torch.sigmoid instead.
  warnings.warn("nn.functional.sigmoid is deprecated. Use torch.sigmoid instead.")
| end of epoch   1 | time:  0.13s | train_loss 14.7669 | valid rse 0.2224 | valid rae 0.2292 | valid corr  0.7993
| end of epoch   2 | time:  0.12s | train_loss 10.9979 | valid rse 0.2366 | valid rae 0.2354 | valid corr  0.7962
| end of epoch   3 | time:  0.15s | train_loss 9.2647 | valid rse 0.1752 | valid rae 0.1958 | valid corr  0.7657
| end of epoch   4 | time:  0.16s | train_loss 7.9519 | valid rse 0.1509 | valid rae 0.1712 | valid corr  0.7268
| end of epoch   5 | time:  0.14s | train_loss 7.0702 | valid rse 0.1506 | valid rae 0.1626 | valid corr  0.7385
test rse 0.3072 | test rae 0.3085 | test corr 0.8084
| end of epoch   6 | time:  0.15s | train_loss 6.2891 | valid rse 0.1479 | valid rae 0.1521 | valid corr  0.7683
| end of epoch   7 | time:  0.14s | train_loss 6.0751 | valid rse 0.1488 | valid rae 0.1477 | valid corr  0.7833
| end of epoch   8 | time:  0.14s | train_loss 6.0787 | valid rse 0.1564 | valid rae 0.1567 | valid corr  0.7760
| end of epoch   9 | time:  0.11s | train_loss 5.5804 | valid rse 0.1726 | valid rae 0.1662 | valid corr  0.7644
| end of epoch  10 | time:  0.11s | train_loss 5.2066 | valid rse 0.1732 | valid rae 0.1656 | valid corr  0.7717
test rse 0.3353 | test rae 0.3171 | test corr 0.7926
| end of epoch  11 | time:  0.11s | train_loss 5.0683 | valid rse 0.1711 | valid rae 0.1656 | valid corr  0.7698
| end of epoch  12 | time:  0.11s | train_loss 4.9801 | valid rse 0.1736 | valid rae 0.1645 | valid corr  0.7717
| end of epoch  13 | time:  0.13s | train_loss 4.8396 | valid rse 0.1646 | valid rae 0.1625 | valid corr  0.7623
| end of epoch  14 | time:  0.11s | train_loss 4.7175 | valid rse 0.1495 | valid rae 0.1513 | valid corr  0.7591
| end of epoch  15 | time:  0.11s | train_loss 4.6493 | valid rse 0.1549 | valid rae 0.1543 | valid corr  0.7519
test rse 0.3173 | test rae 0.3127 | test corr 0.7766
| end of epoch  16 | time:  0.11s | train_loss 4.5070 | valid rse 0.1307 | valid rae 0.1463 | valid corr  0.7526
| end of epoch  17 | time:  0.11s | train_loss 4.3833 | valid rse 0.1470 | valid rae 0.1500 | valid corr  0.7283
| end of epoch  18 | time:  0.10s | train_loss 4.3444 | valid rse 0.1353 | valid rae 0.1376 | valid corr  0.7624
| end of epoch  19 | time:  0.11s | train_loss 4.2395 | valid rse 0.1269 | valid rae 0.1448 | valid corr  0.7656
| end of epoch  20 | time:  0.11s | train_loss 4.1177 | valid rse 0.1298 | valid rae 0.1345 | valid corr  0.7625
test rse 0.2981 | test rae 0.2995 | test corr 0.7933
| end of epoch  21 | time:  0.11s | train_loss 4.0790 | valid rse 0.1235 | valid rae 0.1412 | valid corr  0.7788
| end of epoch  22 | time:  0.11s | train_loss 4.0765 | valid rse 0.1336 | valid rae 0.1532 | valid corr  0.7807
| end of epoch  23 | time:  0.11s | train_loss 3.9592 | valid rse 0.1305 | valid rae 0.1544 | valid corr  0.7867
| end of epoch  24 | time:  0.11s | train_loss 3.9199 | valid rse 0.1325 | valid rae 0.1523 | valid corr  0.7868
| end of epoch  25 | time:  0.11s | train_loss 3.8663 | valid rse 0.1182 | valid rae 0.1383 | valid corr  0.7952
test rse 0.2795 | test rae 0.3031 | test corr 0.8179
| end of epoch  26 | time:  0.11s | train_loss 3.8018 | valid rse 0.1133 | valid rae 0.1303 | valid corr  0.7659
| end of epoch  27 | time:  0.11s | train_loss 3.8342 | valid rse 0.1208 | valid rae 0.1415 | valid corr  0.7918
| end of epoch  28 | time:  0.11s | train_loss 3.9110 | valid rse 0.1251 | valid rae 0.1442 | valid corr  0.7819
| end of epoch  29 | time:  0.11s | train_loss 3.9133 | valid rse 0.1193 | valid rae 0.1432 | valid corr  0.7803
| end of epoch  30 | time:  0.12s | train_loss 3.8179 | valid rse 0.1259 | valid rae 0.1414 | valid corr  0.7664
test rse 0.2933 | test rae 0.3104 | test corr 0.8036
| end of epoch  31 | time:  0.11s | train_loss 3.6832 | valid rse 0.1215 | valid rae 0.1378 | valid corr  0.7888
| end of epoch  32 | time:  0.11s | train_loss 3.6172 | valid rse 0.1236 | valid rae 0.1464 | valid corr  0.7935
| end of epoch  33 | time:  0.11s | train_loss 3.6040 | valid rse 0.1332 | valid rae 0.1602 | valid corr  0.7978
| end of epoch  34 | time:  0.11s | train_loss 3.5720 | valid rse 0.1309 | valid rae 0.1498 | valid corr  0.7946
| end of epoch  35 | time:  0.11s | train_loss 3.6332 | valid rse 0.1157 | valid rae 0.1329 | valid corr  0.7913
test rse 0.2709 | test rae 0.2959 | test corr 0.8205
| end of epoch  36 | time:  0.11s | train_loss 3.6308 | valid rse 0.1256 | valid rae 0.1510 | valid corr  0.8064
| end of epoch  37 | time:  0.11s | train_loss 3.5819 | valid rse 0.1200 | valid rae 0.1443 | valid corr  0.8009
| end of epoch  38 | time:  0.10s | train_loss 3.5450 | valid rse 0.1155 | valid rae 0.1309 | valid corr  0.7887
| end of epoch  39 | time:  0.11s | train_loss 3.4497 | valid rse 0.1286 | valid rae 0.1438 | valid corr  0.7958
| end of epoch  40 | time:  0.11s | train_loss 3.5481 | valid rse 0.1243 | valid rae 0.1423 | valid corr  0.7919
test rse 0.2869 | test rae 0.3092 | test corr 0.8230
| end of epoch  41 | time:  0.11s | train_loss 3.4993 | valid rse 0.1154 | valid rae 0.1349 | valid corr  0.7910
| end of epoch  42 | time:  0.11s | train_loss 3.4429 | valid rse 0.1148 | valid rae 0.1318 | valid corr  0.7927
| end of epoch  43 | time:  0.11s | train_loss 3.4244 | valid rse 0.1198 | valid rae 0.1373 | valid corr  0.7898
| end of epoch  44 | time:  0.11s | train_loss 3.4972 | valid rse 0.1250 | valid rae 0.1451 | valid corr  0.8041
| end of epoch  45 | time:  0.13s | train_loss 3.4081 | valid rse 0.1193 | valid rae 0.1343 | valid corr  0.7967
test rse 0.2743 | test rae 0.2937 | test corr 0.8260
| end of epoch  46 | time:  0.11s | train_loss 3.5217 | valid rse 0.1236 | valid rae 0.1443 | valid corr  0.7995
| end of epoch  47 | time:  0.11s | train_loss 3.4204 | valid rse 0.1163 | valid rae 0.1334 | valid corr  0.7961
| end of epoch  48 | time:  0.11s | train_loss 3.3536 | valid rse 0.1215 | valid rae 0.1432 | valid corr  0.8077
| end of epoch  49 | time:  0.12s | train_loss 3.3236 | valid rse 0.1293 | valid rae 0.1498 | valid corr  0.8010
| end of epoch  50 | time:  0.12s | train_loss 3.3726 | valid rse 0.1238 | valid rae 0.1441 | valid corr  0.8044
test rse 0.2844 | test rae 0.3109 | test corr 0.8282
| end of epoch  51 | time:  0.11s | train_loss 3.2744 | valid rse 0.1210 | valid rae 0.1388 | valid corr  0.8064
| end of epoch  52 | time:  0.13s | train_loss 3.2112 | valid rse 0.1238 | valid rae 0.1406 | valid corr  0.7949
| end of epoch  53 | time:  0.13s | train_loss 3.2257 | valid rse 0.1242 | valid rae 0.1388 | valid corr  0.7978
| end of epoch  54 | time:  0.12s | train_loss 3.2018 | valid rse 0.1288 | valid rae 0.1450 | valid corr  0.7938
| end of epoch  55 | time:  0.13s | train_loss 3.2578 | valid rse 0.1384 | valid rae 0.1592 | valid corr  0.8052
test rse 0.3056 | test rae 0.3327 | test corr 0.8342
| end of epoch  56 | time:  0.11s | train_loss 3.3670 | valid rse 0.1334 | valid rae 0.1404 | valid corr  0.7817
| end of epoch  57 | time:  0.12s | train_loss 3.2539 | valid rse 0.1320 | valid rae 0.1451 | valid corr  0.7893
| end of epoch  58 | time:  0.11s | train_loss 3.2037 | valid rse 0.1350 | valid rae 0.1583 | valid corr  0.8093
| end of epoch  59 | time:  0.11s | train_loss 3.2226 | valid rse 0.1208 | valid rae 0.1325 | valid corr  0.7894
| end of epoch  60 | time:  0.11s | train_loss 3.2380 | valid rse 0.1354 | valid rae 0.1540 | valid corr  0.8002
test rse 0.3005 | test rae 0.3201 | test corr 0.8304
| end of epoch  61 | time:  0.11s | train_loss 3.1653 | valid rse 0.1290 | valid rae 0.1496 | valid corr  0.8046
| end of epoch  62 | time:  0.12s | train_loss 3.1911 | valid rse 0.1272 | valid rae 0.1405 | valid corr  0.7929
| end of epoch  63 | time:  0.11s | train_loss 3.1192 | valid rse 0.1284 | valid rae 0.1497 | valid corr  0.8020
| end of epoch  64 | time:  0.10s | train_loss 3.1526 | valid rse 0.1231 | valid rae 0.1419 | valid corr  0.7981
| end of epoch  65 | time:  0.10s | train_loss 3.0256 | valid rse 0.1184 | valid rae 0.1397 | valid corr  0.8066
test rse 0.2786 | test rae 0.3064 | test corr 0.8320
| end of epoch  66 | time:  0.11s | train_loss 3.0164 | valid rse 0.1289 | valid rae 0.1480 | valid corr  0.8019
| end of epoch  67 | time:  0.11s | train_loss 3.0415 | valid rse 0.1206 | valid rae 0.1391 | valid corr  0.7925
| end of epoch  68 | time:  0.11s | train_loss 3.0729 | valid rse 0.1361 | valid rae 0.1511 | valid corr  0.7925
| end of epoch  69 | time:  0.13s | train_loss 3.0327 | valid rse 0.1354 | valid rae 0.1511 | valid corr  0.7899
| end of epoch  70 | time:  0.11s | train_loss 3.0986 | valid rse 0.1411 | valid rae 0.1629 | valid corr  0.8039
test rse 0.3079 | test rae 0.3311 | test corr 0.8370
| end of epoch  71 | time:  0.12s | train_loss 3.0578 | valid rse 0.1320 | valid rae 0.1485 | valid corr  0.7902
| end of epoch  72 | time:  0.11s | train_loss 3.0759 | valid rse 0.1186 | valid rae 0.1319 | valid corr  0.7953
| end of epoch  73 | time:  0.11s | train_loss 2.9755 | valid rse 0.1262 | valid rae 0.1409 | valid corr  0.8002
| end of epoch  74 | time:  0.11s | train_loss 2.9663 | valid rse 0.1325 | valid rae 0.1529 | valid corr  0.8051
| end of epoch  75 | time:  0.13s | train_loss 3.0464 | valid rse 0.1292 | valid rae 0.1473 | valid corr  0.7969
test rse 0.2943 | test rae 0.3155 | test corr 0.8271
| end of epoch  76 | time:  0.10s | train_loss 2.9908 | valid rse 0.1291 | valid rae 0.1426 | valid corr  0.8035
| end of epoch  77 | time:  0.11s | train_loss 2.9447 | valid rse 0.1359 | valid rae 0.1561 | valid corr  0.8070
| end of epoch  78 | time:  0.10s | train_loss 2.9234 | valid rse 0.1278 | valid rae 0.1429 | valid corr  0.7925
| end of epoch  79 | time:  0.11s | train_loss 2.9473 | valid rse 0.1232 | valid rae 0.1373 | valid corr  0.8005
| end of epoch  80 | time:  0.11s | train_loss 2.9266 | valid rse 0.1243 | valid rae 0.1465 | valid corr  0.8082
test rse 0.2859 | test rae 0.3126 | test corr 0.8419
| end of epoch  81 | time:  0.11s | train_loss 2.8762 | valid rse 0.1191 | valid rae 0.1323 | valid corr  0.8002
| end of epoch  82 | time:  0.11s | train_loss 2.9321 | valid rse 0.1291 | valid rae 0.1424 | valid corr  0.7998
| end of epoch  83 | time:  0.12s | train_loss 2.9012 | valid rse 0.1189 | valid rae 0.1352 | valid corr  0.7985
| end of epoch  84 | time:  0.13s | train_loss 2.8698 | valid rse 0.1282 | valid rae 0.1425 | valid corr  0.7992
| end of epoch  85 | time:  0.12s | train_loss 2.9353 | valid rse 0.1342 | valid rae 0.1549 | valid corr  0.7984
test rse 0.2985 | test rae 0.3192 | test corr 0.8387
| end of epoch  86 | time:  0.11s | train_loss 2.8837 | valid rse 0.1149 | valid rae 0.1276 | valid corr  0.7841
| end of epoch  87 | time:  0.13s | train_loss 2.9011 | valid rse 0.1275 | valid rae 0.1415 | valid corr  0.8026
| end of epoch  88 | time:  0.12s | train_loss 2.8199 | valid rse 0.1227 | valid rae 0.1403 | valid corr  0.7989
| end of epoch  89 | time:  0.11s | train_loss 2.8294 | valid rse 0.1223 | valid rae 0.1413 | valid corr  0.8007
| end of epoch  90 | time:  0.11s | train_loss 2.8238 | valid rse 0.1259 | valid rae 0.1445 | valid corr  0.7977
test rse 0.2893 | test rae 0.3099 | test corr 0.8414
| end of epoch  91 | time:  0.12s | train_loss 2.8325 | valid rse 0.1228 | valid rae 0.1413 | valid corr  0.8031
| end of epoch  92 | time:  0.11s | train_loss 2.8571 | valid rse 0.1233 | valid rae 0.1389 | valid corr  0.7956
| end of epoch  93 | time:  0.11s | train_loss 3.0366 | valid rse 0.1172 | valid rae 0.1290 | valid corr  0.7849
| end of epoch  94 | time:  0.11s | train_loss 2.8872 | valid rse 0.1207 | valid rae 0.1298 | valid corr  0.7788
| end of epoch  95 | time:  0.11s | train_loss 2.7837 | valid rse 0.1186 | valid rae 0.1364 | valid corr  0.7924
test rse 0.2772 | test rae 0.2968 | test corr 0.8375
| end of epoch  96 | time:  0.13s | train_loss 2.7959 | valid rse 0.1182 | valid rae 0.1349 | valid corr  0.7983
| end of epoch  97 | time:  0.11s | train_loss 2.8137 | valid rse 0.1265 | valid rae 0.1418 | valid corr  0.7956
| end of epoch  98 | time:  0.13s | train_loss 2.8141 | valid rse 0.1236 | valid rae 0.1374 | valid corr  0.7963
| end of epoch  99 | time:  0.12s | train_loss 2.8281 | valid rse 0.1276 | valid rae 0.1435 | valid corr  0.7978
| end of epoch 100 | time:  0.14s | train_loss 2.8600 | valid rse 0.1207 | valid rae 0.1339 | valid corr  0.7980
test rse 0.2823 | test rae 0.2967 | test corr 0.8385
test rse 0.2741 | test rae 0.2978 | test corr 0.8062
```
</p>
</details>
