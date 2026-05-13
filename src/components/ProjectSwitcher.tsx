import { useRef, useState } from "react";

import type { StudioProject } from "../store/localStore";
import { getUiText } from "../uiText";

type ProjectSwitcherProps = {
  activeProjectId: string;
  onExport: () => void;
  onImportFile: (file: File) => void | Promise<void>;
  projects: StudioProject[];
  onCreate: (name: string) => void;
  onDelete: (projectId: string) => void;
  onRename: (projectId: string, name: string) => void;
  onSwitch: (projectId: string) => void;
  projectTransferMessage: string | null;
  projectTransferTone: "accent" | "good" | "warn" | "danger";
};

export function ProjectSwitcher({
  activeProjectId,
  onExport,
  onImportFile,
  projects,
  onCreate,
  onDelete,
  onRename,
  onSwitch,
  projectTransferMessage,
  projectTransferTone,
}: ProjectSwitcherProps) {
  const [newProjectName, setNewProjectName] = useState("");
  const [editingProjectId, setEditingProjectId] = useState<string | null>(null);
  const [editingName, setEditingName] = useState("");
  const [confirmProjectId, setConfirmProjectId] = useState<string | null>(null);
  const importInputRef = useRef<HTMLInputElement | null>(null);
  const text = getUiText();

  const activeProject =
    projects.find((project) => project.id === activeProjectId) ?? projects[0] ?? null;

  function handleCreate(): void {
    const trimmedName = newProjectName.trim();
    if (!trimmedName) {
      return;
    }

    onCreate(trimmedName);
    setNewProjectName("");
  }

  function startRename(project: StudioProject): void {
    setEditingProjectId(project.id);
    setEditingName(project.name);
    setConfirmProjectId(null);
  }

  function submitRename(projectId: string): void {
    const trimmedName = editingName.trim();
    if (!trimmedName) {
      return;
    }

    onRename(projectId, trimmedName);
    setEditingProjectId(null);
    setEditingName("");
  }

  function handleImportChange(event: React.ChangeEvent<HTMLInputElement>): void {
    const nextFile = event.target.files?.[0];
    event.target.value = "";

    if (!nextFile) {
      return;
    }

    void onImportFile(nextFile);
  }

  function getTransferLabel(): string {
    if (projectTransferTone === "good") {
      return text.projectSwitcher.success;
    }

    if (projectTransferTone === "danger") {
      return text.projectSwitcher.error;
    }

    if (projectTransferTone === "warn") {
      return text.projectSwitcher.warning;
    }

    return text.projectSwitcher.info;
  }

  return (
    <section className="panel soft">
      <div className="stack">
        <div>
          <strong>{text.projectSwitcher.activeProject}</strong>
          <p className="muted" style={{ marginTop: "0.35rem", marginBottom: 0 }}>
            {activeProject?.name ?? text.projectSwitcher.noProject}
          </p>
        </div>

        <div className="card-list">
          {projects.map((project) => {
            const isActive = project.id === activeProjectId;
            const isEditing = project.id === editingProjectId;
            const isConfirmingDelete = project.id === confirmProjectId;

            return (
              <div key={project.id} className="card">
                <div className="row">
                  <strong>{project.name}</strong>
                  {isActive ? <span className="badge accent">aktiven</span> : null}
                </div>

                {isEditing ? (
                  <div className="stack" style={{ marginTop: "0.8rem" }}>
                    <div className="field">
                      <label htmlFor={`rename-project-${project.id}`}>{text.projectSwitcher.renameProject}</label>
                      <input
                        id={`rename-project-${project.id}`}
                        value={editingName}
                        onChange={(event) => setEditingName(event.target.value)}
                      />
                    </div>
                    <div className="row">
                      <button
                        className="primary"
                        disabled={editingName.trim().length === 0}
                        onClick={() => submitRename(project.id)}
                      >
                        {text.projectSwitcher.saveProjectName}
                      </button>
                      <button
                        onClick={() => {
                          setEditingProjectId(null);
                          setEditingName("");
                        }}
                      >
                        {text.projectSwitcher.cancel}
                      </button>
                    </div>
                  </div>
                ) : (
                  <div className="row" style={{ marginTop: "0.8rem" }}>
                    <button
                      className={isActive ? "secondary" : undefined}
                      onClick={() => onSwitch(project.id)}
                    >
                      {isActive ? text.projectSwitcher.loaded : text.projectSwitcher.switchProject}
                    </button>
                    <button onClick={() => startRename(project)}>{text.projectSwitcher.rename}</button>
                    {isConfirmingDelete ? (
                      <>
                        <button className="primary" onClick={() => onDelete(project.id)}>
                          {text.projectSwitcher.confirmDelete}
                        </button>
                        <button onClick={() => setConfirmProjectId(null)}>{text.projectSwitcher.cancel}</button>
                      </>
                    ) : (
                      <button onClick={() => setConfirmProjectId(project.id)}>{text.projectSwitcher.delete}</button>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>

        <div className="field">
          <label htmlFor="new-project-name">{text.projectSwitcher.newProject}</label>
          <input
            id="new-project-name"
            placeholder={text.projectSwitcher.newProjectPlaceholder}
            value={newProjectName}
            onChange={(event) => setNewProjectName(event.target.value)}
          />
        </div>
        <button
          className="primary"
          disabled={newProjectName.trim().length === 0}
          onClick={handleCreate}
        >
          {text.projectSwitcher.createProject}
        </button>

        <div className="row">
          <button onClick={onExport}>{text.projectSwitcher.exportProject}</button>
          <button onClick={() => importInputRef.current?.click()}>{text.projectSwitcher.importProject}</button>
        </div>
        <input
          ref={importInputRef}
          accept=".json,application/json"
          onChange={handleImportChange}
          style={{ display: "none" }}
          type="file"
        />

        {projectTransferMessage ? (
          <article className="card">
            <div className="row">
              <strong>{text.projectSwitcher.projectTransfer}</strong>
              <span className={`badge ${projectTransferTone}`}>{getTransferLabel()}</span>
            </div>
            <p className="muted" style={{ marginTop: "0.75rem", marginBottom: 0 }}>
              {projectTransferMessage}
            </p>
          </article>
        ) : null}
      </div>
    </section>
  );
}
