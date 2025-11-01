# Deploying to Hugging Face Spaces

This guide will help you deploy this Streamlit application to Hugging Face Spaces using the command line.

## Prerequisites

1. **Hugging Face Account**: Create one at https://huggingface.co/join
2. **Hugging Face CLI**: Install the Hugging Face CLI tool

## Step-by-Step Deployment

### 1. Install Hugging Face CLI

```bash
pip install huggingface_hub[cli]
```

### 2. Login to Hugging Face

```bash
huggingface-cli login
```

Enter your Hugging Face token when prompted. You can get your token from:
https://huggingface.co/settings/tokens

### 3. Create a New Space

Create a new Space on Hugging Face. You can do this via:
- Web UI: Go to https://huggingface.co/new-space
- Or via CLI (recommended):

```bash
huggingface-cli repo create YOUR_SPACE_NAME --type space --sdk streamlit
```

Replace `YOUR_SPACE_NAME` with your desired space name (e.g., `ai-news-summarizer`).

**Note**: The space name must be in the format: `username/space-name` if you want it under your account, or just `space-name` if you're already logged in.

Example:
```bash
huggingface-cli repo create ai-news-summarizer --type space --sdk streamlit
```

### 4. Clone the Space Repository

```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME
```

### 5. Copy Your Project Files

Copy all necessary files to the cloned space directory:

**Files to copy:**
- `app.py` (main entry point)
- `requirements.txt`
- `src/` directory (entire folder)
- `AINews/` directory (entire folder)
- Any configuration files needed

**On Windows (PowerShell):**
```powershell
# From your project root directory
Copy-Item app.py YOUR_SPACE_NAME/
Copy-Item requirements.txt YOUR_SPACE_NAME/
Copy-Item -Recurse src/ YOUR_SPACE_NAME/
Copy-Item -Recurse AINews/ YOUR_SPACE_NAME/
```

**On Linux/Mac:**
```bash
cp app.py requirements.txt YOUR_SPACE_NAME/
cp -r src/ YOUR_SPACE_NAME/
cp -r AINews/ YOUR_SPACE_NAME/
```

### 6. Create README.md in Space (if not exists)

The README.md should include metadata for Hugging Face Spaces. You can copy your existing README or create a new one with the following format:

```markdown
---
title: AI News Summarizer
emoji: 📰
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.28.0
app_file: app.py
pinned: false
---
```

### 7. Add and Commit Files

```bash
cd YOUR_SPACE_NAME
git add .
git commit -m "Initial commit: Deploy AI News Summarizer"
```

### 8. Push to Hugging Face Spaces

```bash
git push
```

### 9. Verify Deployment

Go to your Space URL:
```
https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
```

The Space will automatically build and deploy. This usually takes 2-5 minutes.

## Alternative: Direct Upload (Faster Method)

If you want to deploy without cloning, you can use the `huggingface-cli upload` command:

```bash
# From your project root directory
huggingface-cli upload YOUR_USERNAME/YOUR_SPACE_NAME app.py --repo-type space
huggingface-cli upload YOUR_USERNAME/YOUR_SPACE_NAME requirements.txt --repo-type space
huggingface-cli upload YOUR_USERNAME/YOUR_SPACE_NAME src/ --repo-type space --repo-type space
huggingface-cli upload YOUR_USERNAME/YOUR_SPACE_NAME AINews/ --repo-type space
```

However, the git method is recommended for easier updates.

## Environment Variables

If your app uses API keys (like Groq or Tavily), you'll need to set them as secrets in your Space:

1. Go to your Space settings on Hugging Face
2. Navigate to "Variables and secrets"
3. Add your API keys as secrets (e.g., `GROQ_API_KEY`, `TAVILY_API_KEY`)

Then update your code to read from environment variables:
```python
import os
api_key = os.getenv("GROQ_API_KEY")
```

## Troubleshooting

### Build Fails
- Check `requirements.txt` for any missing dependencies
- Ensure Python version is compatible (Hugging Face Spaces uses Python 3.9 by default)

### App Not Loading
- Verify `app.py` is the correct entry point
- Check that Streamlit is in `requirements.txt`
- Review the build logs in your Space settings

### Module Import Errors
- Ensure all Python files are copied to the Space
- Check that `__init__.py` files exist in package directories

## Updating Your Deployment

After making changes:

```bash
cd YOUR_SPACE_NAME
git add .
git commit -m "Update: [description of changes]"
git push
```

The Space will automatically rebuild with your changes.

