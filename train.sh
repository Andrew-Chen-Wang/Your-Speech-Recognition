# Will work regardless number of times activated
source venv/bin/activate
pip install --upgrade pip wheel setuptools
pip install -r requirements/base.txt
python train.py
pip install --upgrade -e ./DeepSpeech
./DeepSpeech/DeepSpeech.py --n_hidden 2048 --epochs 3 --learning_rate 0.0001 \
  --checkpoint_dir DeepSpeech/fine_tuning_checkpoints/ \
  --train_files training/sets/train.csv --dev_files training/sets/dev.csv \
  --test_files training/sets/test.csv --export_dir output_models/ \
  --use_allow_growth true --use_cudnn_rnn true
