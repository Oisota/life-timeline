CREATE TABLE IF NOT EXISTS "schema_migrations" (version varchar(128) primary key);
CREATE TABLE user (
	id integer primary key autoincrement,
	email text,
	password_hash text
);
CREATE TABLE event (
	id integer primary key autoincrement,
	timestamp integer not null,
	title text not null,
	description text not null,
	user_id integer not null,
	foreign key(user_id) references user(id)
);
-- Dbmate schema migrations
INSERT INTO "schema_migrations" (version) VALUES
  ('20250312001601');
