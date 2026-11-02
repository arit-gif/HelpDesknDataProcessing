import csv
import os

TICKETS_FILE = "tickets.csv"
DATA_FILE = "data_records.csv"
SUMMARY_FILE = "processed_summary.csv"

TICKET_FIELDS = ["ticket_id", "requester", "category", "priority", "status"]
DATA_FIELDS = ["record_id", "department", "metric_name", "numeric_value"]
SUMMARY_FIELDS = ["metric", "value"]


def read_csv(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_csv(filename, fields, rows):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def pause():
    try:
        input("\nPress Enter to continue...")
    except EOFError:
        print()


def add_ticket():
    tickets = read_csv(TICKETS_FILE)
    ticket_id = input("Enter Ticket ID (e.g., T101): ").strip().upper()
    if not ticket_id:
        print("Ticket ID is required.")
        return

    for t in tickets:
        if t["ticket_id"] == ticket_id:
            print("A ticket with this ID already exists.")
            return

    requester = input("Requester Name: ").strip()
    category = input("Category (Hardware/Software/Network): ").strip()
    priority = input("Priority (Low/Medium/High/Critical): ").strip().capitalize()

    if not requester or not category:
        print("Requester Name and Category are required.")
        return

    if priority not in ["Low", "Medium", "High", "Critical"]:
        print("Invalid priority! Choose Low, Medium, High, or Critical.")
        return

    tickets.append({
        "ticket_id": ticket_id,
        "requester": requester,
        "category": category,
        "priority": priority,
        "status": "Open"
    })
    write_csv(TICKETS_FILE, TICKET_FIELDS, tickets)
    print("Ticket added successfully.")


def view_tickets():
    tickets = read_csv(TICKETS_FILE)
    if not tickets:
        print("No tickets found.")
        return

    print(f"\n{'ID':8} {'Requester':14} {'Category':12} {'Priority':10} {'Status'}")
    print("-" * 56)
    for t in tickets:
        print(
            f"{t['ticket_id']:8} {t['requester']:14} "
            f"{t['category']:12} {t['priority']:10} {t['status']}"
        )
    pause()


def search_ticket():
    query = input("Enter Ticket ID, Name, or Priority to search: ").strip().lower()
    if not query:
        print("Please enter something to search for.")
        return

    tickets = read_csv(TICKETS_FILE)
    found = False
    for t in tickets:
        if (query in t["ticket_id"].lower() or
            query in t["requester"].lower() or
            query in t["priority"].lower()):
            print(
                f"{t['ticket_id']} | {t['requester']} | "
                f"{t['category']} | {t['priority']} | {t['status']}"
            )
            found = True

    if not found:
        print("No matching ticket found.")


def update_ticket():
    tickets = read_csv(TICKETS_FILE)
    ticket_id = input("Enter Ticket ID to update: ").strip().upper()

    for t in tickets:
        if t["ticket_id"] == ticket_id:
            new_status = input(
                "Enter new status (Open/In-Progress/Resolved): "
            ).strip().title()
            if new_status not in ["Open", "In-Progress", "Resolved"]:
                print("Invalid status.")
                return
            t["status"] = new_status
            write_csv(TICKETS_FILE, TICKET_FIELDS, tickets)
            print("Ticket status updated successfully.")
            return

    print("Ticket ID not found.")


def delete_ticket():
    tickets = read_csv(TICKETS_FILE)
    ticket_id = input("Enter Ticket ID to delete: ").strip().upper()
    if not ticket_id:
        print("No Ticket ID entered.")
        return

    new_tickets = [t for t in tickets if t["ticket_id"] != ticket_id]
    if len(new_tickets) == len(tickets):
        print("Ticket not found.")
    else:
        write_csv(TICKETS_FILE, TICKET_FIELDS, new_tickets)
        print("Ticket deleted.")


def add_data_record():
    records = read_csv(DATA_FILE)
    record_id = input("Enter Record ID (e.g., R101): ").strip().upper()
    if not record_id:
        print("Record ID is required.")
        return

    for r in records:
        if r["record_id"] == record_id:
            print("Record ID already exists.")
            return

    department = input("Department (e.g., CSE-Lab, Admin): ").strip()
    metric_name = input("Metric Name (e.g., DowntimeMins, Cost): ").strip()
    if not department or not metric_name:
        print("Department and Metric Name are required.")
        return

    try:
        value = float(input("Numeric Value: "))
        if value < 0:
            raise ValueError
    except ValueError:
        print("Enter a valid non-negative number.")
        return

    records.append({
        "record_id": record_id,
        "department": department,
        "metric_name": metric_name,
        "numeric_value": f"{value:.2f}"
    })
    write_csv(DATA_FILE, DATA_FIELDS, records)
    print("Data record saved successfully.")


def view_data_records():
    records = read_csv(DATA_FILE)
    if not records:
        print("No data records found.")
        return

    print(f"\n{'ID':10} {'Department':15} {'Metric':18} {'Value'}")
    print("-" * 53)
    for r in records:
        print(
            f"{r['record_id']:10} {r['department']:15} "
            f"{r['metric_name']:18} {r['numeric_value']}"
        )
    pause()


def process_data_summary():
    records = read_csv(DATA_FILE)
    if not records:
        print("No data records to process.")
        return

    values = []
    for r in records:
        try:
            values.append(float(r["numeric_value"]))
        except ValueError:
            pass

    if not values:
        print("No valid numeric values found.")
        return

    count = len(values)
    total = sum(values)
    average = total / count
    minimum = min(values)
    maximum = max(values)

    print("--- DATA SUMMARY REPORT ---")
    print(f"Total Valid Records : {count}")
    print(f"Sum                 : {total:.2f}")
    print(f"Average             : {average:.2f}")
    print(f"Minimum Value       : {minimum:.2f}")
    print(f"Maximum Value       : {maximum:.2f}")

    summary_rows = [
        {"metric": "Total Valid Records", "value": count},
        {"metric": "Sum", "value": f"{total:.2f}"},
        {"metric": "Average", "value": f"{average:.2f}"},
        {"metric": "Minimum", "value": f"{minimum:.2f}"},
        {"metric": "Maximum", "value": f"{maximum:.2f}"}
    ]
    write_csv(SUMMARY_FILE, SUMMARY_FIELDS, summary_rows)
    print(f"Summary saved to {SUMMARY_FILE}.")


def main():
    while True:
        print("\n=== HELPDESK & DATA PROCESSING SUITE ===")
        print("1. Add Helpdesk Ticket")
        print("2. View Helpdesk Tickets")
        print("3. Search Ticket")
        print("4. Update Ticket Status")
        print("5. Delete Ticket")
        print("6. Add Data Record")
        print("7. View Data Records")
        print("8. Process Data & Export Summary")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            search_ticket()
        elif choice == "4":
            update_ticket()
        elif choice == "5":
            delete_ticket()
        elif choice == "6":
            add_data_record()
        elif choice == "7":
            view_data_records()
        elif choice == "8":
            process_data_summary()
        elif choice == "0":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please select a listed option.")


if __name__ == "__main__":
    main()
