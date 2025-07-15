# 🐚 **Bash Scripting 101: From Basics to Mastery (Lesson 1)**

_📅 KwantaBit CodeLab — Daily Terminal Tips & Bash Series_

---

### 🔰 **What is Bash Scripting?**

**Bash** is a command-line shell and scripting language for Unix-based systems.
It allows you to automate tasks, manage files, install programs, run apps, and more.

A **Bash script** is simply a `.sh` file containing a list of shell commands.

---

## 🧪 **Getting Started – Your First Bash Script**

### ✅ Step 1: Create a file

```bash
nano hello.sh
```

### ✅ Step 2: Write your first script

```bash
#!/bin/bash
echo "Hello from KwantaBit CodeLab!"
```

The first line `#!/bin/bash` is called a **shebang** — it tells the system to use Bash.

### ✅ Step 3: Make it executable

```bash
chmod +x hello.sh
```

### ✅ Step 4: Run it

```bash
./hello.sh
```

✅ Output:

```
Hello from KwantaBit CodeLab!
```

---

## 💡 Common Bash Commands (Beginner Essentials)

| Command      | What it does            |
| ------------ | ----------------------- |
| `ls`         | List directory contents |
| `cd`         | Change directory        |
| `pwd`        | Print working directory |
| `mkdir`      | Make a new directory    |
| `touch file` | Create a new empty file |
| `cp`         | Copy files/directories  |
| `mv`         | Move or rename          |
| `rm`         | Delete files            |
| `cat`        | Display file content    |
| `echo`       | Print to the terminal   |

---

## 🧠 Variables in Bash

```bash
#!/bin/bash

name="Khalid"
echo "Welcome, $name!"
```

Output:

```
Welcome, Khalid!
```

---

## 📥 User Input

```bash
#!/bin/bash

echo "What is your name?"
read username
echo "Hi $username, welcome to Bash scripting!"
```

---

## ⚙️ Conditionals

```bash
#!/bin/bash

age=20

if [ $age -ge 18 ]; then
  echo "You are an adult"
else
  echo "You are underage"
fi
```

✅ `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge` are numeric comparison operators.

---

## 🔁 Loops in Bash

### For Loop

```bash
for i in 1 2 3 4 5
do
  echo "Number: $i"
done
```

### While Loop

```bash
count=1
while [ $count -le 3 ]
do
  echo "Count: $count"
  ((count++))
done
```

---

## 💾 Saving Output to File

```bash
echo "This is a log entry" >> log.txt
```

---

## 🎯 Real-World Mini Example – Backup Script

```bash
#!/bin/bash

echo "Backing up Documents folder..."
cp -r ~/Documents ~/Backup_Documents
echo "Backup complete!"
```

---

## 📌 Next Lessons in the Series:

1. ✅ Intro to Bash Scripting ✔️
2. 🚀 Script Arguments (`$1`, `$2`, etc.)
3. 🔄 Functions and reusability
4. 🔐 Permissions and execution
5. 🧠 Arrays and advanced loops
6. 🛠 Real-world automation: Installers, Auto-Updaters
7. 📦 Deploying scripts on Linux systems (cron jobs, services)

---

📣 _Want more? Stay tuned every morning on **KwantaBit CodeLab** for a new Bash tip or full scripting tutorial._

💡 _Master your tools. Build with Bash._
\#KwantaBit #BashScripting #DevTips #Linux #CLI #Automation #Shell #KwantaBitCodeLab
