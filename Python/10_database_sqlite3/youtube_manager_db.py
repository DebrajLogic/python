import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_videos():
    cursor.execute('''SELECT * FROM videos''')
    videos = cursor.fetchall()
    print('\n')
    print('*' * 70)
    if (not videos):
        print('Videos List Empty!')
    else:
        for video in videos:
            print(video)
    print('*' * 70)


def add_video():
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    cursor.execute(
        '''INSERT INTO videos (name, time) VALUES (?,?)''', (name, time))
    conn.commit()
    print('video added successfully!')


def update_video():
    list_videos()
    video_id = input('Enter video ID to update: ')
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    cursor.execute(
        '''UPDATE videos SET name = ?, time = ? WHERE id = ?''', (name, time, video_id))
    conn.commit()
    print('video updated successfully!')


def delete_video():
    list_videos()
    video_id = input('Enter video ID to delete: ')
    cursor.execute('''DELETE FROM videos WHERE id = ?''', (video_id,))
    conn.commit()
    print('video deleted successfully!')


def main():
    while True:
        print('\n Youtube Manger app with DB')
        print('1. List all videos')
        print('2. Add a video')
        print('3. Update a video')
        print('4. Delete a video')
        print('5. Exit App')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                list_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("Invalid Choice!")

    conn.close()


if __name__ == '__main__':
    main()
