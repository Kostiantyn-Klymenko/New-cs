import sqlite3

conn = sqlite3.connect('library_database.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Book ')
cur.execute('''
CREATE TABLE IF NOT EXISTS Book 
    (
    bookId TEXT PRIMARY KEY,
    cover TEXT NOT NULL,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL,
    pub_year INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    description TEXT NOT NULL
    );
''')

cur.execute('DROP TABLE IF EXISTS Usre ')
cur.execute('''
CREATE TABLE IF NOT EXISTS User 
    (
    userId TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    );
''')

cur.execute('DROP TABLE IF EXISTS Loan ')
cur.execute('''
CREATE TABLE IF NOT EXISTS Loan 
    (
    userId TEXT,
    bookId TEXT,
    loanDate DATE,
    dueDate DATE NOT NULL,
    PRIMARY KEY (userId, bookId, loanDate),
    FOREIGN KEY (userId) REFERENCES User(userId),
    FOREIGN KEY (bookId) REFERENCES Books(bookId)
    );
''')

Books = [
('B0001', 'https://covers.openlibrary.org/b/id/8225631-L.jpg', 'To Kill a Mockingbird', 'Harper Lee', 'Racial Injustice', 1960, 5, 'This novel explores moral growth and racial injustice through the eyes of young Scout Finch. Set in the 1930s Deep South, her father Atticus defends a Black man accused of rape. The story tackles empathy, justice, and prejudice, leaving a lasting impact with its powerful, emotional message and characters.'),
('B0002', 'https://covers.openlibrary.org/b/id/7222246-L.jpg', '1984', 'George Orwell', 'Dystopian Fiction', 1949, 5, 'Orwell\’s dystopian world is governed by Big Brother, where individuality is crushed and truth is manipulated. The novel follows Winston Smith as he secretly rebels against the Party. A chilling look at totalitarianism, surveillance, and propaganda, this book remains deeply relevant in discussions on freedom and personal autonomy.'),
('B0003', 'https://covers.openlibrary.org/b/id/8224813-L.jpg', 'Pride and Prejudice', 'Jane Austen', 'Romantic Fiction', 1813, 4, 'Elizabeth Bennet clashes with the proud Mr. Darcy in this sharp social commentary. Austen\’s romantic classic blends humor, irony, and keen observations on class, marriage, and personal growth. Through misunderstandings and realizations, it ultimately celebrates the triumph of love and mutual respect over pride and social expectation.'),
('B0004', 'https://covers.openlibrary.org/b/id/8225632-L.jpg', 'The Great Gatsby', 'F. Scott Fitzgerald', 'American Classic', 1925, 4, 'Set in the Roaring Twenties, Gatsby throws lavish parties hoping to reunite with his lost love, Daisy. Narrated by Nick Carraway, this tragic tale explores illusions, obsession, and the corruption of the American Dream in a society driven by wealth and desire. A brilliant critique of materialism and lost ideals.'),
('B0005', 'https://covers.openlibrary.org/b/id/6979861-L.jpg', 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, 5, 'Bilbo Baggins is pulled from his peaceful life into a quest with dwarves to reclaim treasure from a dragon. Along the way, he discovers courage, cleverness, and a magical ring. A charming and adventurous prelude to The Lord of the Rings, it\’s a cornerstone of modern fantasy literature.'),
('B0006', 'https://covers.openlibrary.org/b/id/7222242-L.jpg', 'Moby Dick', 'Herman Melville', 'Adventure', 1851, 3, 'Captain Ahab is obsessed with hunting the white whale that maimed him, dragging his crew into a perilous voyage. Narrated by Ishmael, the novel combines philosophical inquiry, detailed maritime knowledge, and intense action. It\’s a dense but powerful meditation on obsession, nature, revenge, and the limits of human understanding.'),
('B0007', 'https://covers.openlibrary.org/b/id/7222250-L.jpg', 'War and Peace', 'Leo Tolstoy', 'Historical Fiction', 1869, 5, 'Tolstoy\’s epic novel intertwines the lives of aristocratic families with the sweeping backdrop of Napoleon\’s invasion of Russia. Rich in detail, it explores love, duty, philosophy, and fate. Through characters like Pierre and Natasha, it captures the emotional and spiritual struggles of individuals caught in the tides of history.'),
('B0008', 'https://covers.openlibrary.org/b/id/8225213-L.jpg', 'Jane Eyre', 'Charlotte Brontë', 'Gothic Fiction', 1847, 4, 'Orphaned and mistreated, Jane Eyre finds work as a governess at Thornfield Hall. There she falls in love with Mr. Rochester, whose secrets test her moral integrity. Blending Gothic atmosphere with social critique, Brontë\’s novel champions emotional strength, independence, and a woman\’s right to her own story.'),
('B0009', 'https://covers.openlibrary.org/b/id/8231994-L.jpg', 'The Catcher in the Rye', 'J.D. Salinger', 'Coming of Age', 1951, 4, 'Holden Caulfield recounts a few days after being expelled from prep school. Wandering through New York, he grapples with isolation, grief, and disillusionment. Narrated in a raw, colloquial voice, this novel captures teenage alienation and the struggle to find meaning in a world full of “phonies.”'),
('B0010', 'https://covers.openlibrary.org/b/id/8168691-L.jpg', 'The Lord of the Rings', 'J.R.R. Tolkien', 'Epic Fantasy', 1954, 5, 'Frodo Baggins carries the One Ring across Middle-earth to destroy it in Mount Doom. Joined by a fellowship of diverse characters, he faces darkness, temptation, and war. Tolkien\’s sweeping epic is a masterclass in worldbuilding, featuring themes of courage, friendship, sacrifice, and the eternal battle between good and evil.'),
('B0011', 'https://covers.openlibrary.org/b/id/8371676-L.jpg', 'Twilight', 'Stephenie Meyer', 'Young Adult', 2005, 2, 'Bella Swan moves to Forks and falls in love with Edward Cullen, a vampire. Their forbidden romance is complicated by supernatural threats and moral dilemmas. The novel explores teenage infatuation, identity, and danger in a modern fantasy setting that sparked a pop culture phenomenon among young adult readers.'),
('B0012', 'https://covers.openlibrary.org/b/id/8221257-L.jpg', 'Fifty Shades of Grey', 'E. L. James', 'Romance', 2011, 1, 'Anastasia Steele becomes entangled in a complex relationship with Christian Grey, a wealthy man with a controlling personality and dark past. This erotic romance explores themes of power, control, and desire. Controversial and widely discussed, the novel gained massive popularity despite divided critical reception.'),
('B0013', 'https://covers.openlibrary.org/b/id/8131770-L.jpg', 'The Da Vinci Code', 'Dan Brown', 'Thriller', 2003, 2, 'When symbologist Robert Langdon investigates a murder at the Louvre, he uncovers secrets that challenge the foundations of Christianity. Following a trail of codes and mysteries, the novel races through Europe with high stakes and conspiracy. A fast-paced thriller mixing history, religion, and suspense to controversial effect.'),
('B0014', 'https://covers.openlibrary.org/b/id/8126181-L.jpg', 'Eragon', 'Christopher Paolini', 'Fantasy', 2002, 2, 'Eragon, a farm boy, discovers a mysterious dragon egg that hatches into Saphira, launching him into a war against an evil empire. With magic, elves, and ancient prophecies, this fantasy adventure draws on classic tropes. Written by a young author, it sparked a new generation\’s interest in epic storytelling.'),
('B0015', 'https://covers.openlibrary.org/b/id/8233779-L.jpg', 'The Alchemist', 'Paulo Coelho', 'Adventure', 1988, 1, 'Santiago, a shepherd, dreams of finding treasure in Egypt and sets off on a journey that becomes spiritual and transformative. Blending mysticism, philosophy, and allegory, Coelho\’s short novel emphasizes following one\’s dreams, listening to the heart, and the interconnectedness of all things. Widely read and inspirational worldwide.'),
('B0016', 'https://covers.openlibrary.org/b/id/8370954-L.jpg', 'The Road', 'Cormac McCarthy', 'Post-Apocalyptic', 2006, 4, 'A father and son travel through a burned-out America, trying to survive. Their journey through ash-covered ruins is grim and sparse, but their bond offers light. McCarthy\’s haunting prose and minimalistic style create a brutal, moving narrative about love, survival, and what it means to carry the fire of humanity.'),
('B0017', 'https://covers.openlibrary.org/b/id/8330471-L.jpg', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Crime', 2005, 4, 'Journalist Mikael Blomkvist and hacker Lisbeth Salander investigate the disappearance of a wealthy girl decades earlier. Their search uncovers dark family secrets and corruption. Combining mystery, social commentary, and complex characters, the novel launches a gripping trilogy that explores violence, justice, and the resilience of outsiders.'),
('B0018', 'https://covers.openlibrary.org/b/id/8370993-L.jpg', 'Gone Girl', 'Gillian Flynn', 'Thriller', 2012, 3, 'On their fifth anniversary, Amy Dunne vanishes, and suspicion falls on her husband, Nick. Through alternating perspectives, the novel unravels a twisted portrait of marriage, deceit, and media manipulation. Flynn\’s psychological thriller grips readers with unreliable narration and shocking revelations that challenge assumptions and redefine the genre.'),
('B0019', 'https://covers.openlibrary.org/b/id/8371640-L.jpg', 'The Fault in Our Stars', 'John Green', 'Young Adult', 2012, 4, 'Hazel and Augustus, two teens with cancer, fall in love while navigating illness, hope, and loss. Told with humor and poignancy, the novel explores mortality, love, and the search for meaning in life\’s brief moments. Green\’s heartfelt writing connects with readers of all ages through its raw emotional honesty.'),
('B0020', 'https://covers.openlibrary.org/b/id/8370987-L.jpg', 'The Hunger Games', 'Suzanne Collins', 'Dystopian', 2008, 4, 'In a dystopian future, Katniss Everdeen volunteers for a deadly televised game to save her sister. As she fights for survival, she becomes a symbol of rebellion. Collins crafts a gripping, violent, and emotionally charged narrative that examines power, resistance, and the cost of entertainment in an oppressive society.'),
('B0021', 'https://covers.openlibrary.org/b/id/8370988-L.jpg', 'Divergent', 'Veronica Roth', 'Dystopian', 2011, 3, 'In a society divided by virtues, Tris discovers she doesn\’t fit into any one group—she\’s Divergent. Facing political turmoil and personal choices, she navigates identity, loyalty, and rebellion. Roth\’s action-packed debut blends coming-of-age and dystopian tension with strong themes of individuality, conformity, and courage.'),
('B0022', 'https://covers.openlibrary.org/b/id/8370991-L.jpg', 'The Maze Runner', 'James Dashner', 'Dystopian', 2009, 3, 'Thomas awakens in a mysterious maze with no memory, surrounded by others also seeking escape. As they face deadly trials, the secrets behind the maze—and the world beyond—slowly unravel. A fast-paced, suspenseful story that launches a series questioning survival, trust, and humanity in a manufactured nightmare.'),
('B0023', 'https://covers.openlibrary.org/b/id/8371049-L.jpg', 'Life of Pi', 'Yann Martel', 'Adventure', 2001, 4, 'After a shipwreck, teenage Pi Patel is stranded in a lifeboat with a Bengal tiger named Richard Parker. Their surreal journey across the ocean blends survival, faith, and storytelling. Martel\’s philosophical novel challenges perceptions of truth and explores the boundaries between fact, fiction, and spiritual belief.'),
('B0024', 'https://covers.openlibrary.org/b/id/8371041-L.jpg', 'Memoirs of a Geisha', 'Arthur Golden', 'Historical Fiction', 1997, 4, 'Sayuri\’s journey from a poor fishing village to becoming one of Kyoto\’s most celebrated geisha is told with elegance and emotional depth. Set in pre- and post-war Japan, the novel explores art, tradition, and female agency in a changing world. A richly detailed and emotionally moving narrative.'),
('B0025', 'https://covers.openlibrary.org/b/id/8371042-L.jpg', 'Water for Elephants', 'Sara Gruen', 'Historical Romance', 2006, 4, 'Jacob Jankowski, a veterinary student, joins a traveling circus during the Great Depression after a family tragedy. There, he finds love and a place among misfits and animals. This novel blends gritty realism with emotional depth, portraying life under the big top and the bonds that can form in unlikely places.'),
('B0026', 'https://covers.openlibrary.org/b/id/8370989-L.jpg', 'A Thousand Splendid Suns', 'Khaled Hosseini', 'Drama', 2007, 5, 'In war-torn Afghanistan, Mariam and Laila, two women from vastly different backgrounds, form a deep and unbreakable bond. Facing abuse, oppression, and loss, their sisterhood becomes a powerful source of hope and resistance. Hosseini\’s novel is a moving tribute to the resilience of Afghan women and the enduring human spirit.'),
('B0027', 'https://covers.openlibrary.org/b/id/8371045-L.jpg', 'The Kite Runner', 'Khaled Hosseini', 'Drama', 2003, 5, 'Amir, haunted by childhood betrayal, returns to a Taliban-ruled Afghanistan to seek redemption. This powerful story explores friendship, guilt, and the chance for atonement. Through its emotional honesty and historical depth, Hosseini\’s debut novel has captivated readers worldwide with its depiction of personal and national transformation.'),
('B0028', 'https://covers.openlibrary.org/b/id/8371043-L.jpg', 'The Book Thief', 'Markus Zusak', 'Historical Fiction', 2005, 5, 'Narrated by Death, this unique novel follows Liesel Meminger, a young girl in Nazi Germany who finds solace in stealing books and sharing them. Amidst war and loss, her love for words provides comfort and connection. A poignant, lyrical tale about the power of literature and humanity\’s resilience in dark times.'),
('B0029', 'https://covers.openlibrary.org/b/id/8370994-L.jpg', 'Room', 'Emma Donoghue', 'Psychological Fiction', 2010, 4, 'Five-year-old Jack lives in a single room with his mother, unaware there\’s a world outside. Told from his perspective, the novel unfolds as they escape captivity and struggle to adjust to freedom. A harrowing yet hopeful story about trauma, recovery, and a mother\’s fierce love and protection.'),
('B0030', 'https://covers.openlibrary.org/b/id/8370990-L.jpg', 'The Lovely Bones', 'Alice Sebold', 'Supernatural Drama', 2002, 4, 'Susie Salmon watches from the afterlife after being murdered at age fourteen. As her family and friends grieve, she follows their struggles to move forward. A blend of crime, grief, and the supernatural, this emotional novel explores how love endures and healing begins even in the face of tragedy.'),
('B0031', 'https://covers.openlibrary.org/b/id/8370986-L.jpg', 'The Time Traveler\’s Wife', 'Audrey Niffenegger', 'Romance', 2003, 4, 'Henry, who involuntarily travels through time, falls in love with Clare, who waits for him in linear time. Their relationship is tested by loss, unpredictability, and fate. Niffenegger\’s novel blends science fiction with deep emotional intimacy, creating a poignant tale about love, longing, and the moments that define us.'),
('B0032', 'https://covers.openlibrary.org/b/id/8371040-L.jpg', 'The Night Circus', 'Erin Morgenstern', 'Fantasy', 2011, 3, 'A mysterious circus appears without warning, enchanting spectators with its magical attractions. Behind the scenes, two young illusionists are bound in a lifelong competition. As love grows between them, the stakes escalate. Morgenstern\’s lyrical debut is a richly imaginative journey full of wonder, romance, and timeless enchantment.'),
('B0033', 'https://covers.openlibrary.org/b/id/8371039-L.jpg', 'Big Little Lies', 'Liane Moriarty', 'Domestic Drama', 2014, 3, 'A murder rocks a quiet seaside town, unraveling the secrets of three women bound by friendship and deception. As their personal lives collide with scandal and lies, the truth behind a tragic event slowly comes to light. Moriarty weaves suspense and social satire into this witty, fast-paced modern drama.'),
('B0034', 'https://covers.openlibrary.org/b/id/8370992-L.jpg', 'Eleanor Oliphant Is Completely Fine', 'Gail Honeyman', 'Contemporary Fiction', 2017, 4, 'Eleanor leads a solitary, tightly structured life until an unexpected friendship changes her world. As she slowly confronts her traumatic past, she begins to heal and rediscover connection. This quirky, touching novel explores loneliness, kindness, and the courage it takes to reach out and accept help.'),
('B0035', 'https://covers.openlibrary.org/b/id/8371038-L.jpg', 'The Midnight Library', 'Matt Haig', 'Philosophical Fiction', 2020, 4, 'Nora Seed enters a magical library that allows her to explore alternate versions of her life. Each book contains a different path she could\’ve taken. As she searches for the perfect life, she discovers what truly matters. A heartfelt exploration of regret, possibility, and the beauty of imperfection.'),
('B0036', 'https://covers.openlibrary.org/b/id/8371044-L.jpg', 'Circe', 'Madeline Miller', 'Mythological Fiction', 2018, 5, 'Circe, daughter of Helios, is banished to an island where she hones her powers and faces legendary figures from Greek mythology. Told from her perspective, the novel reimagines the life of a misunderstood sorceress. Miller\’s poetic prose and feminist lens create a powerful narrative about identity, strength, and transformation.'),
('B0037', 'https://covers.openlibrary.org/b/id/8371047-L.jpg', 'The Seven Husbands of Evelyn Hugo', 'Taylor Jenkins Reid', 'Historical Drama', 2017, 4, 'Hollywood icon Evelyn Hugo finally shares the secrets of her scandalous life with an unknown journalist. Through her seven marriages and personal sacrifices, she reveals the truth behind the glamour. A compelling look at fame, identity, and love in all its complicated forms, set against the golden age of cinema.'),
('B0038', 'https://covers.openlibrary.org/b/id/8371050-L.jpg', 'Daisy Jones & The Six', 'Taylor Jenkins Reid', 'Music Fiction', 2019, 4, 'Told in an oral history format, this novel follows the rise and fall of a fictional 1970s rock band. Behind the fame lies emotional tension, artistic passion, and unresolved love. Reid captures the energy of the era, the messiness of creativity, and the complex dynamics within a band\’s journey.'),
('B0039', 'https://covers.openlibrary.org/b/id/8371046-L.jpg', 'Where the Crawdads Sing', 'Delia Owens', 'Mystery', 2018, 3, 'Kya, the “Marsh Girl,” grows up alone in the wild North Carolina marshes. When a local man is found dead, suspicion turns toward her. Blending mystery, romance, and nature writing, this bestselling novel explores loneliness, resilience, and the deep connection between people and their environment.'),
('B0040', 'https://covers.openlibrary.org/b/id/8371048-L.jpg', 'Verity', 'Colleen Hoover', 'Romantic Thriller', 2018, 3, 'Lowen, a struggling writer, is hired to finish a successful author\’s series after a tragic accident. But she discovers a disturbing manuscript in the author\’s home that reveals chilling secrets. A dark, addictive thriller that blurs the lines between truth and fiction, obsession and love, sanity and madness.'),
('B0041', 'https://covers.openlibrary.org/b/id/8371678-L.jpg', 'It Ends with Us', 'Colleen Hoover', 'Romance', 2016, 3, 'Lily falls for Ryle, a charming neurosurgeon with a dark side, while memories of her first love resurface. As she faces painful truths, she must make impossible choices. A deeply emotional novel that tackles the complexities of abuse, love, and strength through a heartfelt, compassionate lens.'),
('B0042', 'https://covers.openlibrary.org/b/id/8371677-L.jpg', 'Ugly Love', 'Colleen Hoover', 'Romance', 2014, 2, 'Tate falls for Miles, a pilot who refuses to open his heart. Their intense physical relationship becomes emotionally complicated as past trauma surfaces. This steamy, emotionally raw romance delves into grief, love, and the difficult process of healing, with Hoover\’s trademark blend of heartbreak and passion.'),
('B0043', 'https://covers.openlibrary.org/b/id/8371679-L.jpg', 'November 9', 'Colleen Hoover', 'Romance', 2015, 2, 'Fallon and Ben meet on the same day every year, forming a unique connection. Their love story is told through a series of annual reunions, testing fate and trust. With emotional twists and surprising revelations, the novel explores timing, destiny, and the stories we tell ourselves and others.'),
('B0044', 'https://covers.openlibrary.org/b/id/8371675-L.jpg', 'Reminders of Him', 'Colleen Hoover', 'Drama', 2022, 3, 'After serving time for a tragic mistake, Kenna returns to reconnect with her daughter. Facing judgment from the town and the child\’s guardians, she struggles to rebuild her life. A story of redemption, forgiveness, and the lasting effects of grief, told with emotional depth and sincerity.'),
('B0045', 'https://covers.openlibrary.org/b/id/8371674-L.jpg', 'Heart Bones', 'Colleen Hoover', 'Young Adult', 2020, 3, 'Beyah escapes her troubled life to spend the summer with a father she barely knows. There, she meets Samson, a boy with secrets of his own. Together, they navigate heartbreak, trust, and the meaning of home. A tender young adult romance with themes of resilience and second chances.'),
('B0046', 'https://covers.openlibrary.org/b/id/8371673-L.jpg', 'Regretting You', 'Colleen Hoover', 'Family Drama', 2019, 3, 'After a tragic accident, Morgan and her daughter Clara struggle to understand each other and cope with loss. Secrets unravel, testing their bond. Hoover\’s novel examines grief, motherhood, and the pain of growing apart—only to rediscover each other. A moving story about family, forgiveness, and finding your voice.'),
('B0047', 'https://covers.openlibrary.org/b/id/8371672-L.jpg', 'All Your Perfects', 'Colleen Hoover', 'Romance', 2018, 2, 'Quinn and Graham\’s seemingly perfect marriage is falling apart due to infertility struggles. Told in alternating past and present timelines, the novel explores how love can survive disappointment and emotional distance. Hoover\’s portrayal of raw vulnerability makes this a powerful read about the challenges of long-term commitment.'),
('B0048', 'https://covers.openlibrary.org/b/id/8371671-L.jpg', 'Maybe Someday', 'Colleen Hoover', 'Romance', 2014, 2, 'Sydney\’s life changes when she discovers her boyfriend\’s betrayal and moves in with her mysterious neighbor, Ridge. As they write music together, their connection deepens—despite obstacles and complications. This emotional story blends love, creativity, and moral dilemmas with heartfelt intensity and a soundtrack that enhances the reading experience.')
]

cur.executemany("""
INSERT OR IGNORE INTO Book (bookId, cover, title, author, genre, pub_year, rating, description)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", Books)

Users = [
    ('M0001', 'Alice Johnson', 'M0001@email.com', '1bcd'),
    ('M0002', 'Bob Smith', 'M0002@email.com', '3Bcd'),
    ('M0003', 'Charlie Davis', 'M0003@email.com', '6acd'),
    ('M0004', 'Diana Evans', 'M0004@email.com', 'craB'),
    ('M0005', 'Ethan Brown', 'M0005@email.com', '1234'),
    ('M0006', 'Oliver Thompson', 'M0006@email.com', '7thug3821'),
]

cur.executemany("""
INSERT OR IGNORE INTO User (userId, name, email, password)
VALUES (?, ?, ?, ?)
""", Users)

Loans = [
    ('M0001', 'B0001', '2025-02-25', '2025-03-11'),
    ('M0002', 'B0002', '2025-02-28', '2025-03-14'),
    ('M0003', 'B0004', '2025-03-01', '2025-03-15'),
    ('M0004', 'B0005', '2025-03-03', '2025-03-17'),
    ('M0006', 'B0010', '2025-03-05', '2025-03-19'),
]

cur.executemany("""
INSERT OR IGNORE INTO Loan (userId, bookId, loanDate, dueDate)
VALUES (?, ?, ?, ?)
""", Loans)

conn.commit()
conn.close()