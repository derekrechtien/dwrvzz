# Project 2 - Design Focus: Architecture and System Design Process

---

### Group 5
##### Derek Rechtien, Jacob Hollis, Graeson Bullington

---

### Table of Contents

- [Use Case Diagram and Description](#Use-Case-Diagram)

- [Activity Diagram #1](#Activity-Diagram-1)

- [Activity Diagram #2](#Activity-Diagram-2)

- [Activity Diagram #3](#Activity-Diagram-3)

- [Class Diagram](#Class-Diagram)

- [Entity Relationship Diagram](#Entity-Relationship-Diagram)

- [Sequence Diagram](#Sequence-Diagram)

- [State Machine Diagram](#State-Machine-Diagram)

---

### Use Case Diagram
<br>

**Designed by:** *Graeson Bullington*
<br>
**Peer Reviewed by:** *Jacob Hollis and Derek Rechtien*
<br>

<br>

**Caption**: *Use Case diagram showing a set of actions that the assignment submission system should perform in relation to different users*

**Use Case Description**
- Title: Students submitting an assignment for a course

- Description: Students are given assignments by an instructor in a course. Students submit the assignment, which is then graded by teaching assistants (TA). All users (students, TAs, instructors, sys admins) need to log in/out, and all have the ability to use the system to some extent.
- Triggers:
  1. Logging in/out
  2. Submitting assignment
  3. Downloading submission
  4. Opening comments

- Actors: Students, instructors, TAs, sys admins

- Precondition(s): User must be logged in

- Main success scenario: Student can submit assignment, TA can grade that assignment, and all users (aside from sys admin) can see the graded assignment

- Failed End Condition: Student fails to upload the correct file, which triggers error and student is given option to try again

- Extensions
 - Server fails when submission is halfway uploaded
   - System tells student that upload failed and to try again
  - User (any) fails to their correct login credentials
     - System gives option to recover based on either backup email or instructor/TA approval

![ActivityDiagram1](Images/Assignment4UseCaseDiagram.png)

---

### Activity Diagram 1
![ActivityDiagram1](Images/Assignment4ActivityDiagram1.png)

---

### Activity Diagram 2
<br>

**Designed by:** *Graeson Bullington*
<br>
**Peer Reviewed by:** *Jacob Hollis and Derek Rechtien*
<br>

**Activity**: Students submitting an assignment for a course
<br>
**Caption**: *Use Case diagram showing a set of actions that the assignment submission system should perform in relation to different users*
![ActivityDiagram2](Images/Assignment4ActivityDiagram2.png)

---

### Activity Diagram 3
![ActivityDiagram3](Images/Assignment4ActivityDiagram3.png)

---

### Class Diagram
![ClassDiagram](Images/Assignment4ClassDiagram.png)

---

### Entity Relationship Diagram
![EntityRelationshipDiagram](Images/Assignment4ERDiagram.png)

---

### Sequence Diagram
![SequenceDiagram](Images/Assignment4SequenceDiagram.png)

---

### State Machine Diagram
<br>

**Designed by:** *Graeson Bullington*
<br>
**Peer Reviewed by:** *Jacob Hollis and Derek Rechtien*
<br>

**Activity**: Students submitting an assignment for a course
<br>
**Caption**: *State machine diagram showing the discrete behavior of small part of the assignment submission system*

![StateMachineDiagram](Images/Assignment4StateMachineDiagram.png)
