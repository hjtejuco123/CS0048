# 🚌 Bus Ticket Booking System

## 📋 Problem Description
Create a simple bus ticket booking system where users can:
- View available seats
- Book a seat
- Exit the system

The bus starts with **5 seats**. Users can book until no seats are left.

## 🌟 Requirements

### Initialization
- Total seats: **5 available seats** at system start.

### User Interface
Display a menu:
```
1. View Available Seats
2. Book Seat
3. Exit
```
- Prompt the user to **enter a choice**.

### View Available Seats
- If the user selects **option 1**:
  - Display the **current number of available seats**.

### Book Seat
- If the user selects **option 2**:
  1. Check if seats are available.
  2. If seats are available:
     - Prompt the user to **enter their name**.
     - **Record** the booking.
     - **Decrease** the number of available seats by 1.
     - Display a **confirmation** message with:
       - User's name
       - Remaining seats
  3. If **no seats** are available:
     - Display a message: **"Bus is full. No more bookings allowed."**

### Exit
- If the user selects **option 3**:
  - Display a **thank you** message.
  - **Exit** the program.

### Invalid Choice
- If the user enters an invalid input:
  - Display **"Invalid choice. Please try again."**
  - Return to menu.

### Bus Full Handling
- When **all seats** are booked:
  - Display a message: **"Bus is full. No more seats available."**
  - Prevent further bookings.

---
