-- migrate:up
create table user (
	id integer primary key autoincrement,
	email text,
	password_hash text
);

create table event (
	id integer primary key autoincrement,
	timestamp integer not null,
	title text not null,
	description text not null,
	user_id integer not null,
	foreign key(user_id) references user(id)
);

-- migrate:down
drop table event;
drop table user;