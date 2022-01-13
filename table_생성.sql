use bladb;
create table bankaccountlist(
계좌번호 bigint not null,  
이름 varchar(4) not null,
잔액 bigint not null);

create table history(
날짜 varchar(30),
계좌번호 bigint not null,  
이름 varchar(4) not null,
잔액 bigint not null);

