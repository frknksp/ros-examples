# Gazebo Dünya Haritaları

## Modeller

Model dosyalarına aşağıdaki github reposundan ulaşabilirsiniz.


[Dataset-of-Gazebo-Worlds-Models-and-Maps](https://github.com/mlherd/Dataset-of-Gazebo-Worlds-Models-and-Maps)

1. **AWS Small House**
   ![small_house](https://github.com/frknksp/birfen-staj/blob/master/gazebo_world_maps/aws_small_house/small_house.jpg?raw=true)

2. **AWS Bookstore**
   ![bookstore](https://github.com/frknksp/birfen-staj/blob/master/gazebo_world_maps/aws_bookstore/bookstore.jpg?raw=true)

## Haritaların Oluşturulması

Haritalar, `gmapping` yöntemi kullanılarak `roslaunch turtlebot3_slam turtlebot3_slam.launch` komutu ile oluşturulmuştur.

Gmapping, ROS (Robot Operating System) çerçevesinde yaygın olarak kullanılan bir haritalama (SLAM) yöntemidir. Hareketli bir robotun çevresini keşfederek aynı anda konumunu belirlemesini (localization) ve ortamın haritasını oluşturmasını (mapping) sağlar.

Gmapping, bir tarama lazer sensörü (LIDAR) kullanarak çevredeki nesnelerin konumunu algılar ve bu bilgileri kullanarak robotun konumunu günceller ve haritayı oluşturur. Alınan lazer taramaları ve hareket bilgileri kullanılarak, robotun hangi bölgede bulunduğu ve çevresindeki nesnelerin konumu tahmin edilir. Bu bilgiler, SLAM algoritması tarafından işlenerek sürekli olarak güncellenen bir harita oluşturulur.


