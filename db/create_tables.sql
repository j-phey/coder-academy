drop table categories cascade;
drop table items;

-- Categories
CREATE TABLE if not exists categories (
    id serial PRIMARY KEY,
    --  Syntax to create row is [name] [type] [constraints]
    name varchar(50) not null unique, 
    -- 'unique' ensures the rows are unique and no duplicates allowed
    description text
);

-- Insert some rows into categories
insert into categories (name, description) values 
    ('Electronics', 'Gadgets to make life easier'),
    ('Car Parts', 'Expedensive stuff for the box with 4 wheels'),
    ('Sports', 'Get out and play!'),
    ('Video Games', 'Stay in and play!')
;

create table items (
    id serial primary key,

    name varchar(200) not null,
    description text not null,
    
    category_id integer not null,
    foreign key (category_id) references categories (id) on delete cascade 
    -- 'on delete cascade' means if the primary key is deleted, delete the records of the foreign key too (i.e. any references in the 'items' table)
);

insert into items (name, description, category_id) values
    ('Skyrim', 'Awesome open world RPG', 4),
    ('World of Warcraft', 'Popular MMORPG', 4),
    ('iPhone', 'Flagship smartphone by Apple', 1),
    ('Greg Norman golf clubs', 'Look like a pro!', 3);