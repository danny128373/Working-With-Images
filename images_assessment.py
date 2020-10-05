from PIL import Image


word_matrix = Image.open('images/word_matrix.png')
mask = Image.open('images/mask.png')
# resized mask to be the same size as word_matrix
resized_mask = mask.resize(
    (int(mask.size[0]*(word_matrix.size[0]/mask.size[0])), int(mask.size[1]*(word_matrix.size[1]/mask.size[1]))))
# Opacity is now at 128
resized_mask.putalpha(128)
# pasted resized_mask on top of word_matrix
word_matrix.paste(im=resized_mask, box=(0, 0), mask=resized_mask)
# saved the new image with assessment answer
word_matrix.save('images/assessment_answer.png')
