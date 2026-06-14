# CourseSprout - Quick Reference

**Common OpenClaw Commands**

---

## Setup

```
"Test my CourseSprout API connection"
```

---

## Courses

```
"List my CourseSprout courses"
"Get pricing options for course 1"
"List courses in pod 5"
"Create a course called 'AI Mastery'"
"Update course 3 title to 'New Title'"
```

---

## Pods

```
"List my CourseSprout pods"
"Get pricing options for pod 2"
"Create a pod called 'VIP Members'"
"Update pod 4 name to 'Elite'"
```

---

## Members

```
"List all my CourseSprout members"
"Search members for 'john'"
"Get members of course 5"
"Get members with type course"
"Show members of pod 3"
"Find members by pricing option 12"
"Add user John Doe with email john@test.com to pricing option 789"
"Send access email to member 123"
"Send reminder email to pricing option 456"
```

---

## Lessons

```
"Create lesson in course 1, chapter 5: title='Introduction'"
"Add lesson to pod 3, chapter 2: 'Getting Started'"
"Update lesson 10 title to 'Advanced Concepts'"
```

---

## Goals

```
"Create goal for course 1: 'Complete Module 1', type=points, points=100"
"Update goal 3 points to 150"
```

---

## Retrieval

```
"Get badges for course 1"
"Get goals for course 3"
"Get community topics for course 5"
"Get chapters for course 1"
"List chapters in pod 3"
```

---

## Dry-Run (Preview)

```
"Preview creating course 'Test Course' (dry-run)"
"Show what happens if I update pod 3 (don't execute)"
```

---

## Parameters Reference

### Get Members Filters
- `search` - Search by name/email
- `type` - Filter: all, course, membership
- `course_id` - Specific course (requires type=course)
- `pod_id` - Specific pod (requires type=membership)
- `pricing_option_id` - By pricing option
- `per_page` - Results per page (default 10)

### Goal Types
- `points` - Points-based goal (requires points value)
- `badge` - Badge-based goal (requires badge_id)
- `none` - No reward

### Lesson Types
- `video` (default)
- `text`
- Custom types supported

---

## Common Patterns

### Create Course → Add Member
```
1. "Create course 'Marketing 101'"
2. "Get pricing options for course X"  (note pricing_option_id)
3. "Add user John Doe to pricing option Y"
4. "Send access email to member Z"
```

### Create Pod → Add Members → Send Reminder
```
1. "Create pod 'VIP Members'"
2. "Get pricing options for pod X"
3. "Add user Jane Smith to pricing option Y"
4. "Send reminder email to pricing option Y"
```

### Filter Members by Course
```
"Get members with type=course and course_id=5"
```

### Search Members in Pod
```
"Search 'john' in members of pod 3 with type=membership"
```

---

## Safety Notes

⚠️ **Requires Confirmation:**
- All create/update operations
- Email sending
- User management

⚠️ **Bulk Operations:**
- Send Reminder Email targets ALL inactive members

⚠️ **UPSERT Behavior:**
- Add User creates OR updates based on email

---

## Error Codes

- `AUTH_MISSING` - No API key
- `AUTH_INVALID` - Invalid API key
- `NOT_FOUND` - Resource not found
- `VALIDATION_ERROR` - Invalid parameters

---

**Full Documentation:** See `SKILL.md`
