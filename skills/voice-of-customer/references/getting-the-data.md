# Getting the data

The export a tool offers first is often a list of records with no customer words in it. Check that the file holds the text people wrote or said before analysing it. `prepare.py` warns when it does not.

Tools change. Treat this as a guide to what to ask for, and confirm against the tool's own help pages when something has moved.

| Source | What to ask for | Watch for |
| --- | --- | --- |
| Zendesk | The JSON export, which includes ticket comments | The CSV export leaves out comments and descriptions. The JSON export may need turning on by the account owner. |
| Intercom | Conversations through a connected tool, or an API export | The CSV export has no message content. Searches return a few results per page by default. |
| Help Scout, Freshdesk | An export that includes conversation threads | Reporting exports list conversations without their content. |
| Gong and similar call tools | The transcript of each call | "Ask" and "brief" features return summaries. The call-data download is a list of calls, not what was said. |
| Zoom, Google Meet, Teams | The transcript file for each meeting (`.vtt`, `.docx` or a document) | Usually only the organiser can download it. Convert `.docx` to text first. |
| Fathom, Fireflies, Granola, Otter | The full transcript, as text or through a connected tool | Summaries and notes are the tool's interpretation. |
| HubSpot, Salesforce and other CRMs | Deals with their notes, call notes and the closed-lost reason, both the dropdown and any free text | Fields differ in every account. Look at the columns before assuming. |
| Typeform, SurveyMonkey and other survey tools | The full response export as CSV | Summary exports drop the open-ended answers. |
| Your reviews on G2, Capterra or an app store | The export from your own vendor or developer account | Do not collect reviews in bulk from the public pages. |
| Notion, Google Drive, Slack | The specific pages, documents or channel export | Keep it to what the user points at. |

## If you are using a connected tool

- Match on what a tool does, since names differ between agents. You want one that returns full transcripts, messages or comments.
- An authorisation error means the tool is not available. Move to an export and say so.
- Fetch one transcript or conversation at a time, and keep paging until there are no more results.
- Read only. If a tool can also write, do not use those actions.
- Save each fetched item as a file under `research/transcripts/` so it can be prepared and verified like any other.
