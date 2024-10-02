# Bing Daily Wallpaper Setter

This script fetches the daily Bing wallpaper and automatically sets it as the desktop background on **Linux (Ubuntu/GNOME)**, **macOS**, or **Windows**.

## Features
- Fetches the latest Bing wallpaper.
- Automatically updates the wallpaper based on your operating system.
- Supports:
  - **Linux (Ubuntu/GNOME)**
  - **macOS**
  - **Windows**

## Prerequisites

Ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package installer)

Install required Python libraries using:

```bash
pip install requests
# OR
pip install -r requirements.txt
```

## How It Works

1. The script fetches Bing’s daily wallpaper JSON metadata.
2. It downloads the wallpaper image.
3. It automatically updates your desktop wallpaper based on your operating system:
   - **Ubuntu (GNOME)**: Uses `gsettings` to set the wallpaper.
   - **macOS**: Uses `osascript` to update the wallpaper.
   - **Windows**: Uses the `ctypes` library to change the wallpaper.

## Usage

1. Clone or download this repository to your local machine.
2. Run the script with Python:

```bash
python set_wallpaper.py
```

The script will automatically detect your operating system and update the wallpaper accordingly.

---

## Setting up Automatic Wallpaper Updates

You can automate the process of updating your wallpaper daily using a cron job (for Linux/macOS) or a scheduled task (for Windows).

### Linux/macOS (Using Cron Job)

1. Open your terminal.
2. Edit your crontab file using the following command:

   ```bash
   crontab -e
   ```

3. Add the following line to the crontab file to run the script daily at 7 AM:

   ```bash
   0 7 * * * /usr/bin/python3 /path/to/your/script/set_wallpaper.py
   ```

   - **`0 7 * * *`**: This cron expression runs the script every day at 7:00 AM.
   - Replace `/path/to/your/script/set_wallpaper.py` with the actual path to your Python script.

4. Save and exit the crontab editor. Your cron job is now set up to change the wallpaper automatically every day.

### Windows (Using Task Scheduler)

1. Open **Task Scheduler** by searching for it in the Start Menu.
2. Click **Create Basic Task** in the right sidebar.
3. Name your task (e.g., "Bing Wallpaper Update") and click **Next**.
4. Choose **Daily** as the trigger and click **Next**.
5. Set the time (e.g., 7:00 AM) and click **Next**.
6. Select **Start a Program** and click **Next**.
7. In the **Program/script** field, browse to the path of your Python executable (e.g., `python.exe`).
8. In the **Add arguments** field, add the path to your `set_wallpaper.py` script. For example:

   ```bash
   C:\path\to\your\script\set_wallpaper.py
   ```

9. Click **Next** and **Finish**.

Your task is now scheduled to run daily and automatically change the wallpaper.

### Verify the Cron Job/Task Scheduler

- For **Linux/macOS**, you can verify that the cron job is running correctly by checking the cron log:

   ```bash
   grep CRON /var/log/syslog
   ```

- For **Windows**, check the **Task Scheduler Library** to verify the task status and history.
