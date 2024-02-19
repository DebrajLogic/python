import json

fileName = 'videos.txt'


def load_data():
    try:
        with open(fileName, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(fileName, 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print('\n')
    print('*' * 70)
    for index, video in enumerate(videos, start=1):
        print(f'{index}. {video['name']}, Duration: {video['time']}')
    print('*' * 70)


def add_video(videos):
    name = input('Enter a video name: ')
    time = input('Enter duration: ')
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video no to UPDATE: '))
    name = input('Enter a video name: ')
    time = input('Enter duration: ')
    videos[index - 1] = {'name': name, 'time': time}
    save_data_helper(videos)


def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video no to UPDATE: '))
    del videos[index - 1]
    save_data_helper(videos)


def main():
    videos = load_data()
    while True:
        print('\nYOUTUBE MANAGER APP')
        print('1. LIST all videos')
        print('2. ADD a video')
        print('3. UPDATE a video')
        print('4. DELETE a video')
        print('5. Exit')
        choice = input('Enter a choice: ')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('Invalid Choice!')


if __name__ == '__main__':
    main()
