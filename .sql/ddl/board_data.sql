-- auto-generated definition
create table board_data
(
    id              bigint auto_increment
        primary key,
    code            varchar(30)  not null,
    path            varchar(30)  not null,
    name            varchar(30)  not null,
    uri_root        varchar(500) not null,
    model_name      varchar(30)  not null,
    key_name_bid    varchar(30)  not null,
    key_name_page   varchar(30)  null,
    uri_is_fixed    varchar(500) not null,
    uri_link        varchar(500) not null,
    uri_title       varchar(500) not null,
    uri_date        varchar(500) null,
    uri_author      varchar(500) null,
    uri_reference   varchar(500) null,
    uri_inside_date varchar(500) null,
    notice_drop_num int          null,
    constraint board_data_code_uindex
        unique (code)
);

