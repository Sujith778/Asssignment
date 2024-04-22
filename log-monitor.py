import sys
import signal
import re
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle Ctrl+C and exit gracefully
def signal_handler(sig, frame):
    print("\nLog monitoring interrupted. Exiting.")
    sys.exit(0)

# Function to monitor log file
def monitor_log(log_file):
    try:
        with open(log_file, "r") as f:
            f.seek(0, 2)  # Move to the end of the file
            while True:
                line = f.readline()
                if line:
                    # Perform basic analysis on log entries
                    analyze_log_entry(line)
                else:
                    time.sleep(0.1)  # Sleep briefly before checking for new lines
    except FileNotFoundError:
        logger.error(f"Log file '{log_file}' not found.")
        sys.exit(1)

# Function to perform basic analysis on log entries
def analyze_log_entry(log_entry):
    # Count occurrences of specific keywords or patterns
    error_count = len(re.findall(r'ERROR', log_entry))
    if error_count > 0:
        logger.error(f"Error detected in log entry: {log_entry.strip()}")

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python log-monitor.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Start monitoring the log file
    monitor_log(log_file)

if __name__ == "__main__":
    main()
