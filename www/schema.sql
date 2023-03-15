-- 编写mysql脚本

drop database if exists moe; -- 删除数据库
drop user if exists 'exarlos'@'localhost'; -- 删除用户
create database moe; -- 创建数据库
use moe; -- 使用数据库

create user 'exarlos'@'localhost' identified by 'exarlos'; -- 创建用户
alter user 'exarlos'@'localhost' identified with mysql_native_password by '747937aaa';  -- 设置密码
grant select, insert, update, delete on moe.* to 'exarlos'@'localhost'; -- 授权用户

create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8; -- 创建用户表

create table blogs (
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8; -- 创建博客表

create table comments (
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8; -- 创建评论表