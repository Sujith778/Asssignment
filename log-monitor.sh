#!/bin/bash

# Function to monitor log file
monitor_log() {
    clear
    echo "Monitoring log file: $1"
    echo "Press Ctrl+C to stop monitoring"
    tail -f "$1"
}

# Function to perform basic log analysis
analyze_log() {
    echo "Performing basic log analysis on: $1"
    echo "Counting occurrences of error messages:"
    grep -c "ERROR" "$1"
    echo "Generating summary report of top error messages:"
    grep "ERROR" "$1" | sort | uniq -c | sort -nr | head -n 5
}

# Main function
main() {
    # Check if log file is provided as argument
    if [ $# -ne 1 ]; then
        echo "Usage: $0 <log_file>"
        exit 1
    fi

    logfile="$1"

    # Check if log file exists
    if [ ! -f "$logfile" ]; then
        echo "Error: Log file $logfile not found"
        exit 1
    fi

    # Start monitoring log file
    monitor_log "$logfile" &

    # Perform log analysis
    analyze_log "$logfile"
}

# Execute main function with provided arguments
main "$@"