# CourseSprout Skill

**Complete CourseSprout API integration for OpenClaw**

## Quick Start

1. **Set API Key:**
   ```powershell
   $env:COURSESPROUT_API_KEY = "your_api_key_here"
   ```

2. **Test Connection:**
   Ask OpenClaw: "Test my CourseSprout API connection"

3. **Start Using:**
   - "List my CourseSprout courses"
   - "Get members of course 5"
   - "Create a course called 'AI Mastery'"

## Documentation

- **Full Documentation:** See `SKILL.md`
- **API Ingestion Report:** See `coursesprout-api-ingestion.md`
- **Official API Docs:** https://api.coursesprout.com/ai-api-docs

## Features

✅ **21 Endpoints** - Complete API coverage  
✅ **Safety Gates** - All side-effects require confirmation  
✅ **Dry-Run Mode** - Preview operations before executing  
✅ **Smart Validation** - Enum validation, mutually exclusive params  
✅ **Error Handling** - Normalized error responses  
✅ **Pagination** - Laravel pagination support

## Key Operations

### Courses
- List, create, update courses
- Get pricing options
- List by pod

### Memberships (Pods)
- List, create, update pods
- Get pricing options

### Members
- Advanced filtering (type, course, pod, pricing option)
- UPSERT behavior (email-based)
- Send access emails
- Send reminder emails (bulk)

### Lessons
- Create/update lessons
- Support for courses and pods

### Gamification
- Create/update goals
- Points, badges, or none
- Community goals

### AI Retrieval
- Get badges, goals, topics, chapters

## Safety Features

**All destructive operations require confirmation:**
- Create/Update operations
- Email sending
- User management

**Dry-run mode available:**
```
"Preview creating course 'Test' (dry-run)"
```

## Known Quirks

1. **Pod Pricing Endpoint:** Path param named `:course_id` but expects pod ID
2. **POST for Updates:** API uses POST instead of PUT/PATCH
3. **Null Responses:** Many create/update examples show null
4. **Add User:** Returns `user` key instead of `data` key
5. **Get Members:** Uses nested Laravel pagination

**All quirks handled automatically by wrapper.**

## Support

**Issues?** Check `SKILL.md` for complete documentation.
