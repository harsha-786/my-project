#Python script to observe events of operating system and automatically organise files that gets created in test_folder

import time
import logging
import os
import shutil 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

folder_mappings = {
        ".png": "Images",
        ".svg": "SVG files",
        ".tar.gz": "TAR files"
        }

# --- 1. Define the Event Handler ---
# This class will handle what happens when an event is detected.
class MyEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        # This method is called when a file or directory is created.
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            # Here is where you'll add your powerful actions!
            
    def on_modified(self, event):
        # This method is called when a file is modified.
        if not event.is_directory:
            print(f"File modified: {event.src_path}")

# --- 2. Set Up the Observer ---
if __name__ == "__main__":
    # Configure basic logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # The path to watch 
    path = "../../../Desktop/test_folder" 

    # Create the handler and the observer
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True) # recursive=True watches subdirectories

    # Start the observer
    observer.start()
    print(f"Guardian is now watching the folder: {path}")

    try:
        # Keep the script running until you press Ctrl+C
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nGuardian has stopped watching.")
    observer.join()


