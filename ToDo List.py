"""
📝 SIMPLE TO-DO LIST
A clean, professional command-line task manager
Author: [Your Name]
"""

import os

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def add_task(self):
        """Add a new task to the list"""
        task = input("\n📝 Enter your task: ").strip()
        if task:
            self.tasks.append(task)
            print(f"✅ Added: '{task}'")
        else:
            print("❌ Task cannot be empty")
    
    def view_tasks(self):
        """Display all tasks with numbers"""
        if not self.tasks:
            print("\n📭 Your to-do list is empty.")
            print("   Use option 1 to add a task.")
        else:
            print("\n" + "=" * 40)
            print("   📋 YOUR TO-DO LIST")
            print("=" * 40)
            for i, task in enumerate(self.tasks, 1):
                print(f"   {i}. {task}")
            print("=" * 40)
            print(f"   📌 Total: {len(self.tasks)} tasks")
    
    def run(self):
        """Main program loop"""
        print("\n" + "=" * 40)
        print("   📚 SIMPLE TO-DO LIST")
        print("   Python Project 1")
        print("=" * 40)
        
        while True:
            print("\n" + "-" * 40)
            print("   1. ➕ Add a task")
            print("   2. 📋 View all tasks")
            print("   3. 🚪 Exit")
            print("-" * 40)
            
            choice = input("\nChoose (1-3): ")
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                print("\n👋 Goodbye!")
                print(f"   You added {len(self.tasks)} task(s).")
                break
            else:
                print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    app = TodoList()
    app.run()
