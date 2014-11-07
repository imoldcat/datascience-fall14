rm products_learned_settings
rm products_training.json
rm products_out.csv
python product_dedup.py
ruby eval.rb
