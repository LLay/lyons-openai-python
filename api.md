# Shared Types

```python
from openaix.types import ErrorObject, FunctionDefinition, FunctionParameters
```

# Completions

Types:

```python
from openaix.types import Completion, CompletionChoice, CompletionUsage
```

Methods:

- <code title="post /completions">client.completions.<a href="./src/openaix/resources/completions.py">create</a>(\*\*<a href="src/openaix/types/completion_create_params.py">params</a>) -> <a href="./src/openaix/types/completion.py">Completion</a></code>

# Chat

## Completions

Types:

```python
from openaix.types.chat import (
    ChatCompletion,
    ChatCompletionAssistantMessageParam,
    ChatCompletionChunk,
    ChatCompletionContentPart,
    ChatCompletionContentPartImage,
    ChatCompletionContentPartText,
    ChatCompletionFunctionCallOption,
    ChatCompletionFunctionMessageParam,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionMessageToolCall,
    ChatCompletionNamedToolChoice,
    ChatCompletionRole,
    ChatCompletionSystemMessageParam,
    ChatCompletionTokenLogprob,
    ChatCompletionTool,
    ChatCompletionToolChoiceOption,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam,
)
```

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/openaix/resources/chat/completions.py">create</a>(\*\*<a href="src/openaix/types/chat/completion_create_params.py">params</a>) -> <a href="./src/openaix/types/chat/chat_completion.py">ChatCompletion</a></code>

# Embeddings

Types:

```python
from openaix.types import CreateEmbeddingResponse, Embedding
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/openaix/resources/embeddings.py">create</a>(\*\*<a href="src/openaix/types/embedding_create_params.py">params</a>) -> <a href="./src/openaix/types/create_embedding_response.py">CreateEmbeddingResponse</a></code>

# Files

Types:

```python
from openaix.types import FileContent, FileDeleted, FileObject
```

Methods:

- <code title="post /files">client.files.<a href="./src/openaix/resources/files.py">create</a>(\*\*<a href="src/openaix/types/file_create_params.py">params</a>) -> <a href="./src/openaix/types/file_object.py">FileObject</a></code>
- <code title="get /files/{file_id}">client.files.<a href="./src/openaix/resources/files.py">retrieve</a>(file_id) -> <a href="./src/openaix/types/file_object.py">FileObject</a></code>
- <code title="get /files">client.files.<a href="./src/openaix/resources/files.py">list</a>(\*\*<a href="src/openaix/types/file_list_params.py">params</a>) -> <a href="./src/openaix/types/file_object.py">SyncPage[FileObject]</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/openaix/resources/files.py">delete</a>(file_id) -> <a href="./src/openaix/types/file_deleted.py">FileDeleted</a></code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/openaix/resources/files.py">content</a>(file_id) -> HttpxBinaryResponseContent</code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/openaix/resources/files.py">retrieve_content</a>(file_id) -> str</code>
- <code>client.files.<a href="./src/openaix/resources/files.py">wait_for_processing</a>(\*args) -> FileObject</code>

# Images

Types:

```python
from openaix.types import Image, ImagesResponse
```

Methods:

- <code title="post /images/variations">client.images.<a href="./src/openaix/resources/images.py">create_variation</a>(\*\*<a href="src/openaix/types/image_create_variation_params.py">params</a>) -> <a href="./src/openaix/types/images_response.py">ImagesResponse</a></code>
- <code title="post /images/edits">client.images.<a href="./src/openaix/resources/images.py">edit</a>(\*\*<a href="src/openaix/types/image_edit_params.py">params</a>) -> <a href="./src/openaix/types/images_response.py">ImagesResponse</a></code>
- <code title="post /images/generations">client.images.<a href="./src/openaix/resources/images.py">generate</a>(\*\*<a href="src/openaix/types/image_generate_params.py">params</a>) -> <a href="./src/openaix/types/images_response.py">ImagesResponse</a></code>

# Audio

## Transcriptions

Types:

```python
from openaix.types.audio import Transcription
```

Methods:

- <code title="post /audio/transcriptions">client.audio.transcriptions.<a href="./src/openaix/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/openaix/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/openaix/types/audio/transcription.py">Transcription</a></code>

## Translations

Types:

```python
from openaix.types.audio import Translation
```

Methods:

- <code title="post /audio/translations">client.audio.translations.<a href="./src/openaix/resources/audio/translations.py">create</a>(\*\*<a href="src/openaix/types/audio/translation_create_params.py">params</a>) -> <a href="./src/openaix/types/audio/translation.py">Translation</a></code>

## Speech

Methods:

- <code title="post /audio/speech">client.audio.speech.<a href="./src/openaix/resources/audio/speech.py">create</a>(\*\*<a href="src/openaix/types/audio/speech_create_params.py">params</a>) -> HttpxBinaryResponseContent</code>

# Moderations

Types:

```python
from openaix.types import Moderation, ModerationCreateResponse
```

Methods:

- <code title="post /moderations">client.moderations.<a href="./src/openaix/resources/moderations.py">create</a>(\*\*<a href="src/openaix/types/moderation_create_params.py">params</a>) -> <a href="./src/openaix/types/moderation_create_response.py">ModerationCreateResponse</a></code>

# Models

Types:

```python
from openaix.types import Model, ModelDeleted
```

Methods:

- <code title="get /models/{model}">client.models.<a href="./src/openaix/resources/models.py">retrieve</a>(model) -> <a href="./src/openaix/types/model.py">Model</a></code>
- <code title="get /models">client.models.<a href="./src/openaix/resources/models.py">list</a>() -> <a href="./src/openaix/types/model.py">SyncPage[Model]</a></code>
- <code title="delete /models/{model}">client.models.<a href="./src/openaix/resources/models.py">delete</a>(model) -> <a href="./src/openaix/types/model_deleted.py">ModelDeleted</a></code>

# FineTuning

## Jobs

Types:

```python
from openaix.types.fine_tuning import FineTuningJob, FineTuningJobEvent
```

Methods:

- <code title="post /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/openaix/resources/fine_tuning/jobs.py">create</a>(\*\*<a href="src/openaix/types/fine_tuning/job_create_params.py">params</a>) -> <a href="./src/openaix/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}">client.fine_tuning.jobs.<a href="./src/openaix/resources/fine_tuning/jobs.py">retrieve</a>(fine_tuning_job_id) -> <a href="./src/openaix/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/openaix/resources/fine_tuning/jobs.py">list</a>(\*\*<a href="src/openaix/types/fine_tuning/job_list_params.py">params</a>) -> <a href="./src/openaix/types/fine_tuning/fine_tuning_job.py">SyncCursorPage[FineTuningJob]</a></code>
- <code title="post /fine_tuning/jobs/{fine_tuning_job_id}/cancel">client.fine_tuning.jobs.<a href="./src/openaix/resources/fine_tuning/jobs.py">cancel</a>(fine_tuning_job_id) -> <a href="./src/openaix/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/events">client.fine_tuning.jobs.<a href="./src/openaix/resources/fine_tuning/jobs.py">list_events</a>(fine_tuning_job_id, \*\*<a href="src/openaix/types/fine_tuning/job_list_events_params.py">params</a>) -> <a href="./src/openaix/types/fine_tuning/fine_tuning_job_event.py">SyncCursorPage[FineTuningJobEvent]</a></code>

# Beta

## Assistants

Types:

```python
from openaix.types.beta import (
    Assistant,
    AssistantDeleted,
    AssistantStreamEvent,
    AssistantTool,
    CodeInterpreterTool,
    FunctionTool,
    MessageStreamEvent,
    RetrievalTool,
    RunStepStreamEvent,
    RunStreamEvent,
    ThreadStreamEvent,
)
```

Methods:

- <code title="post /assistants">client.beta.assistants.<a href="./src/openaix/resources/beta/assistants/assistants.py">create</a>(\*\*<a href="src/openaix/types/beta/assistant_create_params.py">params</a>) -> <a href="./src/openaix/types/beta/assistant.py">Assistant</a></code>
- <code title="get /assistants/{assistant_id}">client.beta.assistants.<a href="./src/openaix/resources/beta/assistants/assistants.py">retrieve</a>(assistant_id) -> <a href="./src/openaix/types/beta/assistant.py">Assistant</a></code>
- <code title="post /assistants/{assistant_id}">client.beta.assistants.<a href="./src/openaix/resources/beta/assistants/assistants.py">update</a>(assistant_id, \*\*<a href="src/openaix/types/beta/assistant_update_params.py">params</a>) -> <a href="./src/openaix/types/beta/assistant.py">Assistant</a></code>
- <code title="get /assistants">client.beta.assistants.<a href="./src/openaix/resources/beta/assistants/assistants.py">list</a>(\*\*<a href="src/openaix/types/beta/assistant_list_params.py">params</a>) -> <a href="./src/openaix/types/beta/assistant.py">SyncCursorPage[Assistant]</a></code>
- <code title="delete /assistants/{assistant_id}">client.beta.assistants.<a href="./src/openaix/resources/beta/assistants/assistants.py">delete</a>(assistant_id) -> <a href="./src/openaix/types/beta/assistant_deleted.py">AssistantDeleted</a></code>

### Files

Types:

```python
from openaix.types.beta.assistants import AssistantFile, FileDeleteResponse
```

Methods:

- <code title="post /assistants/{assistant_id}/files">client.beta.assistants.files.<a href="./src/openaix/resources/beta/assistants/files.py">create</a>(assistant_id, \*\*<a href="src/openaix/types/beta/assistants/file_create_params.py">params</a>) -> <a href="./src/openaix/types/beta/assistants/assistant_file.py">AssistantFile</a></code>
- <code title="get /assistants/{assistant_id}/files/{file_id}">client.beta.assistants.files.<a href="./src/openaix/resources/beta/assistants/files.py">retrieve</a>(file_id, \*, assistant_id) -> <a href="./src/openaix/types/beta/assistants/assistant_file.py">AssistantFile</a></code>
- <code title="get /assistants/{assistant_id}/files">client.beta.assistants.files.<a href="./src/openaix/resources/beta/assistants/files.py">list</a>(assistant_id, \*\*<a href="src/openaix/types/beta/assistants/file_list_params.py">params</a>) -> <a href="./src/openaix/types/beta/assistants/assistant_file.py">SyncCursorPage[AssistantFile]</a></code>
- <code title="delete /assistants/{assistant_id}/files/{file_id}">client.beta.assistants.files.<a href="./src/openaix/resources/beta/assistants/files.py">delete</a>(file_id, \*, assistant_id) -> <a href="./src/openaix/types/beta/assistants/file_delete_response.py">FileDeleteResponse</a></code>

## Threads

Types:

```python
from openaix.types.beta import Thread, ThreadDeleted
```

Methods:

- <code title="post /threads">client.beta.threads.<a href="./src/openaix/resources/beta/threads/threads.py">create</a>(\*\*<a href="src/openaix/types/beta/thread_create_params.py">params</a>) -> <a href="./src/openaix/types/beta/thread.py">Thread</a></code>
- <code title="get /threads/{thread_id}">client.beta.threads.<a href="./src/openaix/resources/beta/threads/threads.py">retrieve</a>(thread_id) -> <a href="./src/openaix/types/beta/thread.py">Thread</a></code>
- <code title="post /threads/{thread_id}">client.beta.threads.<a href="./src/openaix/resources/beta/threads/threads.py">update</a>(thread_id, \*\*<a href="src/openaix/types/beta/thread_update_params.py">params</a>) -> <a href="./src/openaix/types/beta/thread.py">Thread</a></code>
- <code title="delete /threads/{thread_id}">client.beta.threads.<a href="./src/openaix/resources/beta/threads/threads.py">delete</a>(thread_id) -> <a href="./src/openaix/types/beta/thread_deleted.py">ThreadDeleted</a></code>
- <code title="post /threads/runs">client.beta.threads.<a href="./src/openaix/resources/beta/threads/threads.py">create_and_run</a>(\*\*<a href="src/openaix/types/beta/thread_create_and_run_params.py">params</a>) -> <a href="./src/openaix/types/beta/threads/run.py">Run</a></code>
- <code>client.beta.threads.<a href="./src/openaix/resources/beta/threads/threads.py">create_and_run_stream</a>(\*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]</code>

### Runs

Types:

```python
from openaix.types.beta.threads import RequiredActionFunctionToolCall, Run, RunStatus
```

Methods:

- <code title="post /threads/{thread_id}/runs">client.beta.threads.runs.<a href="./src/openaix/resources/beta/threads/runs/runs.py">create</a>(thread_id, \*\*<a href="src/openaix/types/beta/threads/run_create_params.py">params</a>) -> <a href="./src/openaix/types/beta/threads/run.py">Run</a></code>
- <code title="get /threads/{thread_id}/runs/{run_id}">client.beta.threads.runs.<a href="./src/openaix/resources/beta/threads/runs/runs.py">retrieve</a>(run_id, \*, thread_id) -> <a href="./src/openaix/types/beta/threads/run.py">Run</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}">client.beta.threads.runs.<a href="./src/openaix/resources/beta/threads/runs/runs.py">update</a>(run_id, \*, thread_id, \*\*<a href="src/openaix/types/beta/threads/run_update_params.py">params</a>) -> <a href="./src/openaix/types/beta/threads/run.py">Run</a></code>
- <code title="get /threads/{thread_id}/runs">client.beta.threads.runs.<a href="./src/openaix/resources/beta/threads/runs/runs.py">list</a>(thread_id, \*\*<a href="src/openaix/types/beta/threads/run_list_params.py">params</a>) -> <a href="./src/openaix/types/beta/threads/run.py">SyncCursorPage[Run]</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}/cancel">client.beta.threads.runs.<a href="./src/openaix/resources/beta/threads/runs/runs.py">cancel</a>(run_id, \*, thread_id) -> <a href="./src/openaix/types/beta/threads/run.py">Run</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}/submit_tool_outputs">client.beta.threads.runs.<a href="./src/openaix/resources/beta/threads/runs/runs.py">submit_tool_outputs</a>(run_id, \*, thread_id, \*\*<a href="src/openaix/types/beta/threads/run_submit_tool_outputs_params.py">params</a>) -> <a href="./src/openaix/types/beta/threads/run.py">Run</a></code>
- <code>client.beta.threads.runs.<a href="./src/openaix/resources/beta/threads/runs/runs.py">create_and_stream</a>(\*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]</code>
- <code>client.beta.threads.runs.<a href="./src/openaix/resources/beta/threads/runs/runs.py">submit_tool_outputs_stream</a>(\*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]</code>

#### Steps

Types:

```python
from openaix.types.beta.threads.runs import (
    CodeInterpreterLogs,
    CodeInterpreterOutputImage,
    CodeInterpreterToolCall,
    CodeInterpreterToolCallDelta,
    FunctionToolCall,
    FunctionToolCallDelta,
    MessageCreationStepDetails,
    RetrievalToolCall,
    RetrievalToolCallDelta,
    RunStep,
    RunStepDelta,
    RunStepDeltaEvent,
    RunStepDeltaMessageDelta,
    ToolCall,
    ToolCallDelta,
    ToolCallDeltaObject,
    ToolCallsStepDetails,
)
```

Methods:

- <code title="get /threads/{thread_id}/runs/{run_id}/steps/{step_id}">client.beta.threads.runs.steps.<a href="./src/openaix/resources/beta/threads/runs/steps.py">retrieve</a>(step_id, \*, thread_id, run_id) -> <a href="./src/openaix/types/beta/threads/runs/run_step.py">RunStep</a></code>
- <code title="get /threads/{thread_id}/runs/{run_id}/steps">client.beta.threads.runs.steps.<a href="./src/openaix/resources/beta/threads/runs/steps.py">list</a>(run_id, \*, thread_id, \*\*<a href="src/openaix/types/beta/threads/runs/step_list_params.py">params</a>) -> <a href="./src/openaix/types/beta/threads/runs/run_step.py">SyncCursorPage[RunStep]</a></code>

### Messages

Types:

```python
from openaix.types.beta.threads import (
    Annotation,
    AnnotationDelta,
    FileCitationAnnotation,
    FileCitationDeltaAnnotation,
    FilePathAnnotation,
    FilePathDeltaAnnotation,
    ImageFile,
    ImageFileContentBlock,
    ImageFileDelta,
    ImageFileDeltaBlock,
    Message,
    MessageContent,
    MessageContentDelta,
    MessageDeleted,
    MessageDelta,
    MessageDeltaEvent,
    Text,
    TextContentBlock,
    TextDelta,
    TextDeltaBlock,
)
```

Methods:

- <code title="post /threads/{thread_id}/messages">client.beta.threads.messages.<a href="./src/openaix/resources/beta/threads/messages/messages.py">create</a>(thread_id, \*\*<a href="src/openaix/types/beta/threads/message_create_params.py">params</a>) -> <a href="./src/openaix/types/beta/threads/message.py">Message</a></code>
- <code title="get /threads/{thread_id}/messages/{message_id}">client.beta.threads.messages.<a href="./src/openaix/resources/beta/threads/messages/messages.py">retrieve</a>(message_id, \*, thread_id) -> <a href="./src/openaix/types/beta/threads/message.py">Message</a></code>
- <code title="post /threads/{thread_id}/messages/{message_id}">client.beta.threads.messages.<a href="./src/openaix/resources/beta/threads/messages/messages.py">update</a>(message_id, \*, thread_id, \*\*<a href="src/openaix/types/beta/threads/message_update_params.py">params</a>) -> <a href="./src/openaix/types/beta/threads/message.py">Message</a></code>
- <code title="get /threads/{thread_id}/messages">client.beta.threads.messages.<a href="./src/openaix/resources/beta/threads/messages/messages.py">list</a>(thread_id, \*\*<a href="src/openaix/types/beta/threads/message_list_params.py">params</a>) -> <a href="./src/openaix/types/beta/threads/message.py">SyncCursorPage[Message]</a></code>

#### Files

Types:

```python
from openaix.types.beta.threads.messages import MessageFile
```

Methods:

- <code title="get /threads/{thread_id}/messages/{message_id}/files/{file_id}">client.beta.threads.messages.files.<a href="./src/openaix/resources/beta/threads/messages/files.py">retrieve</a>(file_id, \*, thread_id, message_id) -> <a href="./src/openaix/types/beta/threads/messages/message_file.py">MessageFile</a></code>
- <code title="get /threads/{thread_id}/messages/{message_id}/files">client.beta.threads.messages.files.<a href="./src/openaix/resources/beta/threads/messages/files.py">list</a>(message_id, \*, thread_id, \*\*<a href="src/openaix/types/beta/threads/messages/file_list_params.py">params</a>) -> <a href="./src/openaix/types/beta/threads/messages/message_file.py">SyncCursorPage[MessageFile]</a></code>
