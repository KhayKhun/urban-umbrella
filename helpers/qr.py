import qrcode
img = qrcode.make('https://cuwgzhmuoktlapqmmspk.supabase.co/storage/v1/object/public/food_images/photo_2024-05-26_20-33-55.jpg')

img.save("kuku.png")