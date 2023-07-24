
# # Cartographer ROS Integration

Cartographer, robotların çevrelerinin bir haritasını oluşturmasına ve aynı zamanda bu haritada kendi konumlarını belirlemesine olanak tanıyan bir SLAM (Simultane Lokalizasyon ve Haritalama) yöntemidir. Lidar ve odometri gibi çeşitli sensörleri kullanarak haritalar oluşturur.

## SLAM Yaklaşımı

Cartographer, SLAM için iki aşamalı bir yaklaşım izler:

1. **Sparse Map Building (Seyrek Harita Oluşturma):** İlk aşamada, Cartographer, lidar verilerini kullanarak çevrenin seyrek bir haritasını oluşturur. Bu seyrek harita, ikinci aşamayı başlatmak için kullanılır ve robotun başlangıç konumunu belirlemekte önemlidir.

2. **Pose Graph Optimization (Konumlandırma Grafiği Optimizasyonu):** İkinci aşama, konumlandırma grafiği optimizasyonu ile detaylı haritalama işlemine odaklanır. Cartographer, İteratif En Yakın Nokta (ICP) ve Levenberg-Marquardt algoritmaları gibi sofistike algoritmaları kullanarak haritayı ve robotun hareket yolunu iyileştirir. Bu süreç, lidar ve odometri verilerini etkin bir şekilde birleştirerek son derece doğru ve detaylı haritalar oluşturur.

## Özellikler

Cartographer, ROS2 için tasarlanmış bir SLAM paketidir ve robotların çeşitli ortamlarda doğru ve detaylı haritalar oluşturmasını sağlar. Temel özellikleri şunlardır:

- Lidar ve odometri gibi çeşitli sensörleri destekler.
- Çok çeşitli robotlar ve uygulamalar için kullanılabilir.
- Kullanımı kolay ve ayarlanabilir bir yöntemdir.
- Son derece doğru ve detaylı haritalar oluşturur.

Cartographer, otonom araçlar, robotik kolları ve mobil robotlar gibi birçok farklı robotik uygulamada yaygın olarak kullanılmaktadır.

## .lua Konfigürasyon Dosyası

Cartographer ROS2 entegrasyonunu yapılandırmak için .lua uzantılı bir konfigürasyon dosyası kullanılır. Bu dosya, çeşitli parametreleri içerir ve sistem nasıl çalışacağını, hangi sensörlerin ve çerçevelerin kullanılacağını belirler. Aşağıda dosyada bulunan parametreler ve açıklamaları verilmiştir:

1. **map_frame:** Alt haritaları yayınlamak için kullanılacak ROS çerçeve kimliği, genellikle "map" olarak ayarlanır. (Örnek Değer: "map")

2. **tracking_frame:** SLAM algoritması tarafından izlenen çerçeve kimliği. Genellikle "imu_link" olarak tercih edilir. (Örnek Değer: "imu_link", "base_link")

3. **published_frame:** Pose'ları yayınlamak için kullanılacak ROS çerçeve kimliği. Örneğin, başka bir sistemden "odom" çerçevesi sağlanıyorsa "odom" olarak ayarlanır. (Örnek Değer: "odom" veya "base_link")

4. **odom_frame:** "provide_odom_frame" etkinleştirilmişse, yerel SLAM sonuçlarını yayınlamak için kullanılacak çerçeve. (Örnek Değer: "odom")

5. **provide_odom_frame:** Etkinleştirilirse, yerel, döngü kapatılmamış sürekli pose, "odom_frame" olarak "map_frame" içinde yayınlanır. (Örnek Değer: true veya false)

6. **publish_frame_projected_to_2d:** Etkinleştirilirse, yayınlanan pose 2D pose olarak sınırlanır. Bu, 2D modda istenmeyen düzlem dışı pozları önlemek için yapılır. (Örnek Değer: true veya false)

7. **use_odometry:** Etkinleştirilirse, "odom" konusunda nav_msgs/Odometry mesajlarına abone olur. (Örnek Değer: true veya false)

8. **use_nav_sat:** Etkinleştirilirse, "fix" konusunda sensor_msgs/NavSatFix mesajlarına abone olur. (Örnek Değer: true veya false)

9. **use_landmarks:** Etkinleştirilirse, "landmarks" konusunda cartographer_ros_msgs/LandmarkList mesajlarına abone olur. (Örnek Değer: true veya false)

10. **num_laser_scans:** Abone olunacak lazer tarama konusu sayısı. Bir lazer tarayıcı için "scan" konusunda sensor_msgs/LaserScan'a abone olur, birden fazla lazer tarayıcı için "scan_1", "scan_2", vb. gibi konulara abone olur.  (Örnek Değer: 1)

11. **num_multi_echo_laser_scans:** Abone olunacak çoklu yankılı lazer tarama konusu sayısıdır. Bir çoklu yankılı lazer tarayıcı için "echoes" konusunda sensor_msgs/MultiEchoLaserScan'a abone olur, birden fazla çoklu yankılı lazer tarayıcı için "echoes_1", "echoes_2", vb. gibi konulara abone olur.  (Örnek Değer: 0)

12. **num_subdivisions_per_laser_scan:** Alınan (çoklu yankılı) lazer taramasını kaç parçaya böleceğini belirler. Bir taramayı bölmek, tarayıcıların hareket halindeyken tarayıcıları düzleştirmeyi mümkün kılar. Buna karşılık gelen bir iz yapıcı seçeneği, bölen taramaları bir nokta bulutu haline getirmek için kullanılacaktır ve bu tarama eşleştirmesi için kullanılacaktır.  (Örnek Değer: 1)

13. **num_point_clouds:** Abone olunacak nokta bulutu konusu sayısı. Bir menzil bulucu için "points2" konusunda sensor_msgs/PointCloud2'ye abone olur, birden fazla menzil bulucu için "points2_1", "points2_2", vb. gibi konulara abone olur.  (Örnek Değer: 0)

14. **lookup_transform_timeout_sec:** tf2 kullanarak dönüşümleri aramak için kullanılacak zaman aşımı süresi (saniye cinsinden).  (Örnek Değer: 0.2)

15. **submap_publish_period_sec:** Alt harita pozlarını yayınlamak için kullanılacak aralık (saniye cinsinden).  (Örnek Değer: 0.3)

16. **pose_publish_period_sec:** Pose'ları yayınlamak için kullanılacak aralık (saniye cinsinden).  (Örnek Değer: 5e-3 (200 Hz frekans için)

17. **publish_to_tf:** TF dönüşümlerini sağlamayı etkinleştirir veya devre dışı bırakır.  (Örnek Değer: true veya false)

18. **publish_tracked_pose:** Takip edilen pose'ları geometry_msgs/PoseStamped türünde "tracked_pose" konusuna yayınlamayı etkinleştirir.  (Örnek Değer: true veya false)

19. **trajectory_publish_period_sec:** İzlemeyi yayınlamak için kullanılacak aralık (saniye cinsinden).  (Örnek Değer: 30e-3 (30 milisaniye için)

20. **rangefinder_sampling_ratio:** Menzil bulucu(telemetre) mesajları için sabit oranlı örnekleme.  (Örnek Değer: 0.1 veya 0.5)

21. **odometry_sampling_ratio:** Odometri mesajları için sabit oranlı örnekleme.   (Örnek Değer: 0.1 veya 0.5)

22. **fixed_frame_sampling_ratio:** Sabit çerçeve mesajları için sabit oranlı örnekleme.   (Örnek Değer: 0.1 veya 0.5)

23. **imu_sampling_ratio:** IMU mesajları için sabit oranlı örnekleme.   (Örnek Değer: 0.1 veya 0.5)

24. **landmarks_sampling_ratio:** Landmark mesajları için sabit oranlı örnekleme.   (Örnek Değer: 0.1 veya 0.5)

Bu parametreler, Cartographer ROS2 entegrasyonunun çeşitli konfigürasyon ayarlarını kontrol etmek için kullanılır. Uygulamanıza ve donanımınıza uygun değerleri seçerek, Cartographer'ı belirli bir çevre veya robot için optimize edebilirsiniz.

Google'ın kendi dökümanına ulaşmak için [linke](https://google-cartographer-ros.readthedocs.io/en/latest/index.html) tıklayabilirsiniz.
