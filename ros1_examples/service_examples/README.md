# Action ve Service

Action ve Service, Robot Operating System (ROS) alanında kullanılan terimlerdir ve ROS tarafından sağlanan iletişim mekanizmalarını ifade eder.

## Service (Servis)

ROS Service, bir ROS düğümünden diğerine yapılan bir çağrı aracılığıyla belirli bir işlevi gerçekleştiren bir iletişim mekanizmasıdır. Service çağrısı istemci (client) ve hizmet sunucusu (server) arasında gerçekleşir. İstemci, bir hizmet sunucusuna belirli bir talepte bulunur ve hizmet sunucusu bu talebi alır, işler ve sonucu istemciye geri döner.

Servisler, senkron iletişim sağlar, yani istemci bir talepte bulunduktan sonra cevap gelene kadar bekler. Servisler, genellikle bir hizmetin birden çok parametreyle çağrılmasını sağlar ve sonuç olarak bir yanıt döndürür. Örneğin, bir hizmet, iki sayıyı toplamak veya bir sensör değerini okumak gibi bir işlevi gerçekleştirebilir.

## Action (Eylem)

ROS Action, genellikle bir uzun süreli görevin gerçekleştirilmesi için kullanılan bir iletişim mekanizmasıdır. Eylemler, bir hedef (goal), geri bildirim (feedback) ve sonuç (result) olmak üzere üç bileşenden oluşur. Hedef, eylemin gerçekleştirmek istediği görevi tanımlar, geri bildirim, eylem sürecinde ilerleme hakkında bilgi sağlar ve sonuç, eylemin tamamlandığını veya başarısız olduğunu bildirir.

Eylemler, asenkron iletişim sağlar, yani istemci, eylemin sonucunu beklemek zorunda kalmadan diğer işlemleri devam ettirebilir. Eylemler, genellikle uzun süren veya potansiyel olarak kesintiye uğrayan işlemleri temsil etmek için kullanılır. Örneğin, bir robotun belirli bir konuma gitmesi veya bir nesneyi algılaması gibi görevler bir eylem aracılığıyla gerçekleştirilebilir.

## Action ile Service Arasındaki Farklar

Action ve Service arasındaki temel farklar şunlardır:

1. İletişim Mekanizması: Servisler, senkron iletişim sağlarken, eylemler asenkron iletişim sağlar.
2. Yapı: Servisler basit bir istek-yanıt mekanizmasına sahiptir, ancak eylemler hedef, geri bildirim ve sonuç olmak üzere daha karmaşık bir yapıya sahiptir.
3. Kullanım Senaryosu: Servisler, kısa süreli işlemler için kullanılırken, eylemler genellikle uzun süreli ve potansiyel olarak kesintiye uğrayan görevler için kullanılır.
4. Kullanım Durumu: Servisler, bir hizmetin anında sonucunu almak için kullanılırken, eylemler daha uzun süreli işlemlerde geri bildirim almayı sağlar.
Bu farklar, ROS tabanlı sistemlerde Action ve Service arasındaki tercihi belirlerken dikkate alınmalıdır. İşlevsel gereksinimlere ve iletişim şekline bağlı olarak, bir servis veya bir eylem kullanmak daha uygun olabilir.
