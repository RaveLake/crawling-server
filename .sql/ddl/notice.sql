-- auto-generated definition
create table notice
(
    id         bigint auto_increment
        primary key,
    bid        bigint               not null,
    code       varchar(30)          not null,
    is_fixed   tinyint(1) default 0 not null,
    title      varchar(200)         not null,
    link       varchar(500)         not null,
    date       date                 null,
    author     varchar(30)          null,
    reference  varchar(50)          null,
    created_at datetime             not null
);

