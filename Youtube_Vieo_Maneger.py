"""youtube video manager is a kind of project where you can add your favrioute video name and the duration of 
the video . you can see lsit of all videos , add new video, update and delete . we will save all the informatin
in a file  name youtube.txt . while saving info we use json to save the info in json format."""


import json

file_name = "youtube.txt"
def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_data_to_file(video):
    with open(file_name,"w") as file:
        json.dump(video, file)

def list_all_videos(videos):
    print("Your List: ")
    print("*" * 120)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video.get('name')} , {video['duration']}")
    print("\n")    
    print("*" * 120)

def add_video(videos):
    name = input("Enter a Video Name: ")
    duration= input("Enter a video duration: ")
    videos.append({'name':name, 'duration':duration})
    save_data_to_file(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to update"))
    if (1<= index <= len(videos)):
        name = input("Enter a Video Name: ")
        duration= input("Enter a video duration: ")
        videos[index-1] = {'name':name, 'duration':duration}
        save_data_to_file(videos)
        print("Updated")
    else:
        print("Enter a valid number")
    



def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to Delete"))
    if (1<= index <= len(videos)):
        del videos[index-1] 
        save_data_to_file(videos)
        print("Deleted")
    else:
        print("Enter a valid number")
def main():

    while True:
        videos = load_data()     
        print("\n WELCOME TO YOUTUBE VIDEO MANAGER")
        print("1. List all the videos")
        print("2. Add new video to List")
        print("3. update the current video from List")
        print("4. Delete the video from the list")
        print("5. Exit the program")
        choice = input("Enter Your Choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")

if __name__ == '__main__':
    main()

            