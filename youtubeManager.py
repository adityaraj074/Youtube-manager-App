import sqlite3

conn = sqlite3.connect('youtube_video.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
        )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("No videos available.")
    else:
        print("\nList of Videos:")
        for index, row in enumerate(rows, start=1): 
            print(f"{index}. {row[1]}, {row[2]}")

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print(f"'{name}' added successfully!")

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    print(f"Video ID '{video_id}' updated successfully!")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()
    print(f"Video ID '{video_id}' deleted successfully!")

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)  
        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id) 
        elif choice == "5":
            break
        else:
            print("Invalid Choice ") 
            
    conn.close()
        
               
if __name__ == "__main__":
    main()
