drop table categories cascade;
drop table items;

-- Categories
create table if not exists categories (
    id serial primary key,
    --  Syntax to create row is [name] [type] [constraints]
    name varchar(50) not null unique, 
    -- 'unique' ensures the rows are unique and no duplicates allowed
    description text
);

-- Insert some rows into categories
insert into categories (name, description) values 
    ('Electronics', 'Gadgets to make life easier'),
    ('Car Parts', 'Expensive stuff for the box with 4 wheels'),
    ('Sports', 'Get out and play!'),
    ('Video Games', 'Stay in and play!')
;

create table items (
    id serial primary key,

    name varchar(200) not null,
    description text not null,
    
    category_id integer not null,
    foreign key (category_id) references categories (id)
);