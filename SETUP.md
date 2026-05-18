# Manual Setup Steps

This document outlines the manual steps required to complete the SecondBrain setup after the automated structure has been created.

## Step 1: Install Syncthing

### macOS
```bash
brew install syncthing
```

### Windows
Download from: https://syncthing.net/downloads/

Start Syncthing:
```bash
syncthing
```

The web UI will open at http://localhost:8384

## Step 2: Configure Syncthing Folder Sharing

### On Primary Device (Mac)

1. Open Syncthing web UI (http://localhost:8384)
2. Click "Add Folder"
3. Configure:
   - **Folder Label**: SecondBrain
   - **Folder Path**: /Users/josemariabarbeito/PycharmProjects/SecondBrain
   - **Folder Type**: Send & Receive
   - **Share with devices**: Select your secondary device

4. Click "Save"

5. In folder settings (edit the folder):
   - **Watch for Changes**: Enabled
   - **Rescan Interval**: 60s
   - **Filesystem Watching**: Enabled
   - **Ignore Permissions**: Enabled
   - **Versioning**: Staggered File Versioning
     - **Keep**: 30 days

### On Secondary Device (Windows)

1. Open Syncthing web UI (http://localhost:8384)
2. Accept the folder share from the primary device
3. Configure:
   - **Folder Path**: C:\Users\YourUsername\SecondBrain
   - **Folder Type**: Send & Receive
   - **Watch for Changes**: Enabled
   - **Rescan Interval**: 60s
   - **Filesystem Watching**: Enabled
   - **Ignore Permissions**: Enabled
   - **Versioning**: Staggered File Versioning
     - **Keep**: 30 days

### Important Notes

- Share ONLY the SecondBrain folder
- DO NOT share: desktop, documents, home directory
- The .stignore file is already configured to exclude volatile files
- Both devices must be online for sync to occur

## Step 3: Install Obsidian Plugins

Open the SecondBrain vault in Obsidian, then:

1. Go to Settings > Community Plugins
2. Turn on "Community Plugins"
3. Click "Browse" and install the following plugins:

### Required Plugins

1. **Dataview**
   - Purpose: Structured querying and data views
   - Enable after installation

2. **Templater**
   - Purpose: Dynamic templates with scripting
   - Enable after installation
   - Configure template folder: Projects/Templates

3. **QuickAdd**
   - Purpose: Fast capture and workflow automation
   - Enable after installation

4. **Calendar**
   - Purpose: Daily notes calendar view
   - Enable after installation
   - Configure:
     - Create daily notes in: Daily/
     - Date format: YYYY-MM-DD

5. **Tasks**
   - Purpose: Task management with queries
   - Enable after installation

6. **Omnisearch**
   - Purpose: Better search functionality
   - Enable after installation

7. **Smart Connections**
   - Purpose: AI semantic linking
   - Enable after installation
   - Requires initial indexing (run when vault is stable)

8. **Excalidraw**
   - Purpose: Visual thinking and diagrams
   - Enable after installation

### Plugin Configuration

#### Templater
- Template folder location: Projects/Templates
- Date format: YYYY-MM-DD
- Time format: HH:mm:ss

#### Daily Notes (if using built-in instead of Calendar)
- New file location: Daily/
- Date format: YYYY-MM-DD
- Template file: Projects/Templates/daily-note.md

## Step 4: Configure GitHub Remote

### Create Private Repository

1. Go to GitHub.com
2. Create a new private repository named "secondbrain"
3. DO NOT initialize with README (we already have one)

### Connect Remote

```bash
cd /Users/josemariabarbeito/PycharmProjects/SecondBrain
git remote add origin https://github.com/yourusername/secondbrain.git
git branch -M main
git push -u origin main
```

Replace `yourusername` with your actual GitHub username.

## Step 5: Verify Setup

### Validation Checklist

- [ ] Syncthing is running on both devices
- [ ] Syncthing shows both devices as connected
- [ ] SecondBrain folder appears in Syncthing on both devices
- [ ] Obsidian opens the SecondBrain vault successfully
- [ ] All plugins are installed and enabled
- [ ] Create a test note in Obsidian
- [ ] Test note appears on secondary device via Syncthing
- [ ] No .sync-conflict files appear
- [ ] Git push to GitHub works
- [ ] Windsurf can open the workspace and index files

### Test Sync Workflow

1. On Mac: Create a test note in Knowledge/test.md
2. Wait 60 seconds (or trigger manual rescan in Syncthing)
3. On Windows: Verify test.md appears
4. On Windows: Edit the note
5. On Mac: Verify changes appear
6. Commit and push to Git
7. Verify on GitHub

## Step 6: Configure Windsurf (if needed)

The vault is already configured as a Windsurf workspace. Verify:

- Windsurf can open the SecondBrain directory
- Markdown files are indexed
- Scripts/ directory is accessible
- Relative paths work correctly

## Troubleshooting

### Syncthing Not Syncing

- Check both devices are online
- Verify folder paths match exactly
- Check Syncthing web UI for errors
- Ensure .stignore is not blocking needed files
- Restart Syncthing on both devices

### Obsidian Plugins Not Loading

- Check Obsidian is updated to latest version
- Restart Obsidian after plugin installation
- Check plugin documentation for dependencies
- Disable and re-enable problematic plugins

### Git Conflicts

- Pull before pushing: `git pull origin main`
- Resolve conflicts manually
- Never use `git push --force` on shared vault
- Use Syncthing for real-time sync, Git for backups

### .sync-conflict Files

- These appear when both devices edit the same file offline
- Compare both versions manually
- Merge changes into the main file
- Delete the conflict file
- Review .stignore if conflicts persist

## Ongoing Maintenance

### Weekly

- Commit and push changes to Git
- Review and process Inbox.md into permanent notes
- Check for .sync-conflict files

### Monthly

- Review Syncthing versioning (keeps 30 days)
- Update Obsidian plugins
- Test sync workflow
- Backup vault to external storage (optional)

### After Major Changes

- Commit to Git with descriptive message
- Test sync on secondary device
- Verify no conflicts arise
