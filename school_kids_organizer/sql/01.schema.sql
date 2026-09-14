CREATE TABLE public.child (
	child_id serial4 NOT NULL,
	first_name varchar(100) NULL,
	last_name varchar(100) NULL,
	gender varchar(10) NULL,
	birth_date date NULL,
	street varchar(100) NULL,
	house_number varchar(50) NULL,
	postal_code varchar(50) NULL,
	city varchar(100) NULL,
	group_id int4 NULL,
	contact_person varchar(100) NULL,
	contact_number varchar(50) NULL,
	created_at timestamptz DEFAULT CURRENT_TIMESTAMP NULL,
	CONSTRAINT child_gender_check CHECK (((gender)::text = ANY ((ARRAY['male'::character varying, 'female'::character varying])::text[]))),
	CONSTRAINT child_pkey PRIMARY KEY (child_id),
	CONSTRAINT fkey_child_group FOREIGN KEY (group_id) REFERENCES public.kindergarten_groups(group_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE public.kindergarten_groups (
	group_id serial4 NOT NULL,
	"name" varchar(25) NULL,
	min_age int4 NULL,
	max_age int4 NULL,
	capacity int4 NULL,
	CONSTRAINT check_age_range CHECK ((min_age < max_age)),
	CONSTRAINT kindergarten_groups_capacity_check CHECK ((capacity > 0)),
	CONSTRAINT kindergarten_groups_max_age_check CHECK ((max_age > 0)),
	CONSTRAINT kindergarten_groups_min_age_check CHECK ((min_age >= 0)),
	CONSTRAINT kindergarten_groups_pkey PRIMARY KEY (group_id)
);

select * from child;
select * from kindergarten_groups kg;
