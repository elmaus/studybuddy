import sqlite3

def get_cards(deck):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM cards WHERE deck=:deck", {'deck':deck})
    items = c.fetchall()
    conn.close()
    return items

def create_card(side_a, side_b, rarity, deck):
    conn = sqlite3.connect('databese.db')
    c = conn.cursor()

    c.execute("INSERT INTO card VALUE (:side_a, :side_b, :rarity, :deck)", {'side_a':side_a, 'side_b':side_b, 'rarity':rarity, 'deck':deck})
    conn.commit()
    conn.close()

def get_deck(deck):
    conn = sqlite3.connect('databese.db')
    c = conn.cursor()

    c.execute("SELECT * FROM deck WHERE deck=:deck", {'deck':deck})
    item = c.fetchone()
    conn.close()
    return item

def create_deck(deck, category):
    conn = sqlite3.connect('databese.db')
    c = conn.cursor()

    c.execute("INSERT INTO deck VALUE (:deck, :category)", {'deck':deck, 'category':category})
    conn.commit()
    conn.close()


def create_deck_category(category):
    conn = sqlite3.connect('databese.db')
    c = conn.cursor()

    c.execute("INSERT INTO deck_category VALUE (:category)", {'category':category})
    conn.commit()
    conn.close()

def get_deck_category(category):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM deck_category WHERE categoty=:category", {'category':category})
    item = c.fetchone()
    conn.close()
    return item[0]

def get_deck_categories():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    items = [item[1] for item in c.execute("SELECT rowid, * FROM deck_category")]
    conn.close()

    return items

def get_all_decks(category):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    items = [item[1] for item in list(c.execute("SELECT rowid, * FROM deck WHERE category=:category", {'category':category}))]

    conn.close()
    return items

def create_flush_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # c.execute("DROP TABLE deck")
    # print("deck table deleted")
    # c.execute("DROP TABLE cards")
    # print("cards table deleted")
    c.execute("""CREATE TABLE deck_category (
        category text PRIMARY KEY
    )
    """)
    print("deck category table created")

    c.execute("""CREATE TABLE deck (
        deck text PRIMARY KEY,
        category text,
        FOREIGN KEY (category)
        REFERENCES deck_category (category)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )
    """)

    print("table deck created")

    c.execute("""CREATE TABLE cards (
        side_a text,
        side_b text,
        rarity integer,
        deck text,
        FOREIGN KEY (deck)
        REFERENCES deck (deck)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )
    """)
    print("table cards created")
    conn.commit()
    conn.close()

def get_notes(category):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    notes = []
    c.execute("SELECT rowid, * FROM notes WHERE category=:category", {'category':category})
    items = c.fetchall()

    conn.close()
    return items

def create_note(category, title, content):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO notes VALUES (:title, :content, :category)", {'title':title, 'content':content, 'category':category})
    conn.commit()
    conn.close()

def update_note(id, title, content):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("""UPDATE notes
        SET title = :title,
            content = :content
        WHERE
            rowid = :id  
    """, {'id':id, 'title':title, 'content':content})
    
    conn.commit()
    conn.close()

def get_categories(subject):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    categories = []
    for cat in list(c.execute("SELECT * FROM categories WHERE subject_name=:subname", {'subname':subject})):
        categories.append(cat[0])

    return categories

def get_category(category):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM categories WHERE category=:category", {'category':category})
    item = c.fetchone()
    conn.close()
    if item:
        return item[0]
    return None

def create_category(category, subject):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO categories VALUES (:category, :subject_name)", {'category':category, 'subject_name':subject})
    conn.commit()
    conn.close()

def get_subjects():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    subjects = []
    for s in list(c.execute("SELECT * FROM subjects")):
        subjects.append(s[0])

    conn.close()
    return subjects

def get_subject(subject):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM subjects WHERE subject_name=:subject_name", {'subject_name':subject})
    item = c.fetchone()[0]
    conn.close()
    return item

def create_subjects():
    subjects = ['Programming', 'Mathematics', 'Science', 'Philosophy', 'Religion']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    for i in subjects:
        c.execute("INSERT INTO subjects VALUES (:subject_name)", {'subject_name': i})

    conn.commit()
    conn.close()

def create_subject(subject):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO subjects VALUES (:subject_name)", {'subject_name':subject})
    conn.commit()
    conn.close()


def create_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE subjects (
        subject_name text PRIMARY KEY
    )
    """)

    c.execute("""CREATE TABLE categories (
        category text PRIMARY KEY,
        subject_name text,
        FOREIGN KEY (subject_name)
        REFERENCES subjects (subject_name)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )
    """)

    c.execute("""CREATE TABLE notes (
        title text,
        content text,
        category text,
        FOREIGN KEY (category)
        REFERENCES categories (category)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()
