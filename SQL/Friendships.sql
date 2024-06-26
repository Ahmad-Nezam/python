INSERT INTO friendships.users (first_name,last_name) VALUES('chris','Baker'),('chris','Baker'),('chris','Baker'),
('diana','Smith'),('james','johnson'),('jessica','davidson')

insert into  friendships.friendships(user_id,friend_id) VALUES (1,6),(1,5),(1,4),(4,1),(5,1),(6,1)

select users.first_name , users.last_name, user2.first_name as friend_first_name,
 user2.last_name as friend_last_name
from users
left join friendships on users.id = friendships.user_id
left join users as user2 on friendships.friend_id = user2.id
order by friend_last_name;