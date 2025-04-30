def split_dataset_sequential(input_file_en, input_file_hi, output_prefix_en, output_prefix_hi, train_ratio, test_ratio, val_ratio):
    with open(input_file_en, 'r', encoding='utf-8') as f_en, open(input_file_hi, 'r', encoding='utf-8') as f_hi:
        lines_en = f_en.readlines()
        lines_hi = f_hi.readlines()

    total_lines = len(lines_en)
    train_size = int(total_lines * train_ratio)
    test_size = int(total_lines * test_ratio)
    val_size = int(total_lines * val_ratio)

    # Split into train, test, and val sets
    train_lines_en = lines_en[:train_size]
    train_lines_hi = lines_hi[:train_size]
    
    test_lines_en = lines_en[train_size:train_size + test_size]
    test_lines_hi = lines_hi[train_size:train_size + test_size]
    
    val_lines_en = lines_en[train_size + test_size:train_size + test_size + val_size]
    val_lines_hi = lines_hi[train_size + test_size:train_size + test_size + val_size]

    # Write to output files
    with open(output_prefix_en + '-train.txt', 'w', encoding='utf-8') as f_en, open(output_prefix_hi + '-train.txt', 'w', encoding='utf-8') as f_hi:
        for en, hi in zip(train_lines_en, train_lines_hi):
            f_en.write(f'{en.strip()}\n')
            f_hi.write(f'{hi.strip()}\n')
    
    with open(output_prefix_en + '-test.txt', 'w', encoding='utf-8') as f_en, open(output_prefix_hi + '-test.txt', 'w', encoding='utf-8') as f_hi:
        for en, hi in zip(test_lines_en, test_lines_hi):
            f_en.write(f'{en.strip()}\n')
            f_hi.write(f'{hi.strip()}\n')

    with open(output_prefix_en + '-val.txt', 'w', encoding='utf-8') as f_en, open(output_prefix_hi + '-val.txt', 'w', encoding='utf-8') as f_hi:
        for en, hi in zip(val_lines_en, val_lines_hi):
            f_en.write(f'{en.strip()}\n')
            f_hi.write(f'{hi.strip()}\n')

# Define input and output file paths and ratios
input_en_file = 'clean_en.txt'
input_hi_file = 'clean_hi.txt'
output_prefix_en = 'src'
output_prefix_hi = 'tgt'
train_ratio = 0.635
test_ratio = 0.174
val_ratio = 0.191

# Split datasets sequentially
split_dataset_sequential(input_en_file, input_hi_file, output_prefix_en, output_prefix_hi, train_ratio, test_ratio, val_ratio)
