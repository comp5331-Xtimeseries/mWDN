python main.py --model=mWDN --data=solar --seq_len=137 --c_in=168 --c_out=137 --levels=1 --save=model/model_solar.pt >log.solar.txt 2>&1 &

CUDA_VISIBLE_DEVICES=1 python main.py --model=mWDN --data=exchange_rate --seq_len=8 --c_in=168 --c_out=8 --levels=1 --gpu=0 --save=model/model_exchange_rate.pt > log.exchange_rate.txt 2>&1 &

python main.py --model=mWDN --data=electricity --seq_len=321 --c_in=168 --c_out=321 --levels=1 --save=model/model_electricity.pt > log.electricity.txt 2>&1 &

python main.py --model=mWDN --data=traffic --seq_len=862 --c_in=168 --c_out=862 --levels=1 --gpu=0 --save=model/model_traffic.pt > log.traffic.txt 2>&1 &

