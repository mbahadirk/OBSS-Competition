import os
import pandas as pd
import cv2

# CSV dosyasını yükle
submission_v1_path = 'submission_v1.csv'
df1 = pd.read_csv(submission_v1_path)

submission_v2_path = 'submission_v2.csv'
df2 = pd.read_csv(submission_v2_path)

submission_v3_path = 'submission_v3.csv'
df3 = pd.read_csv(submission_v3_path)

submission_v4_path = 'submission_v4.csv'
df4 = pd.read_csv(submission_v4_path)

submission_v5_path = 'submission_v5.csv'
df5 = pd.read_csv(submission_v5_path)

submission_v6_path = 'submission_v6.csv'
df6 = pd.read_csv(submission_v6_path)

submission_v7_path = 'submission_v7.csv'
df7 = pd.read_csv(submission_v7_path)

submission_v10_path = 'submission_v10.csv'
df10 = pd.read_csv(submission_v10_path)


# Görsel dizin yolu
image_dir = 'C:/Users/pahstoner/Desktop/obss competition/test/test'

# Her satır için işlemleri gerçekleştir
for index, row in df1.iterrows():
    image_id = row['image_id']
    caption = row['caption']
    caption2 = df2.loc[df2['image_id'] == image_id, 'caption'].values[0]
    caption3 = df3.loc[df3['image_id'] == image_id, 'caption'].values[0]
    caption4 = df4.loc[df4['image_id'] == image_id, 'caption'].values[0]
    caption5 = df5.loc[df5['image_id'] == image_id, 'caption'].values[0]
    caption6 = df6.loc[df6['image_id'] == image_id, 'caption'].values[0]
    caption7 = df7.loc[df7['image_id'] == image_id, 'caption'].values[0]
    caption10 = df10.loc[df10['image_id'] == image_id, 'caption'].values[0]

    image_path = os.path.join(image_dir, f"{image_id}.jpg")

    # Görselin mevcut olup olmadığını kontrol et
    if not os.path.exists(image_path):
        print(f"Uyarı: {image_path} bulunamadı, atlanıyor.")
        continue

    # Görseli yükle
    image = cv2.imread(image_path)

    if image is None:
        print(f"Hata: {image_path} yüklenemedi.")
        continue

    # Görseli göster
    window_title = f"Caption: {caption}"
    print("\n",caption,"\n",caption2,"\n",caption3,"\n",caption4,"\n",caption5,"\n",caption6,"\n",caption7,"\n",caption10)
    cv2.imshow(window_title, image)

    # Bir tuşa basılana kadar bekle
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    os.system('cls')
