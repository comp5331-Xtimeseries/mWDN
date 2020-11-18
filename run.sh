python main.py --model=mWDN --data=solar --seq_len=168 --c_in=137 --c_out=137 --levels=1 --save=model/model_solar.pt >log.solar.txt 2>&1 &

CUDA_VISIBLE_DEVICES=4 python main.py --model=mWDN --data=exchange_rate --seq_len=168 --c_in=8 --c_out=8 --levels=1 --save=model/model_exchange_rate.pt --gpu=0  > log.exchange_rate.txt 2>&1 &

python main.py --model=mWDN --data=electricity --seq_len=168 --c_in=321 --c_out=321 --levels=1 --save=model/model_electricity.pt  > log.electricity.txt 2>&1 &

python main.py --model=mWDN --data=traffic --seq_len=168 --c_in=862 --c_out=862 --levels=1 --save=model/model_traffic.pt > log.traffic.txt 2>&1 &

