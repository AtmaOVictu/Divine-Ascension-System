import { useState } from "react";

import { Panel } from "../components/Panel";
import { formatDate, type DocumentSource, type TruthUnit } from "../domain/types";

type LibraryViewProps = {
  documents: DocumentSource[];
  truthUnits: TruthUnit[];
  onAddDocument: (title: string, content: string) => void;
  onAddSampleDocument: () => void;
};

export function LibraryView(props: LibraryViewProps): JSX.Element {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const submit = (): void => {
    const safeTitle = title.trim();
    const safeContent = content.trim();

    if (!safeTitle || !safeContent) {
      return;
    }

    props.onAddDocument(safeTitle, safeContent);
    setTitle("");
    setContent("");
  };

  return (
    <div className="view-grid">
      <div className="two-column">
        <Panel
          title="Dokumenti v knjižnici"
          rightSlot={
            <div className="row">
              <button className="subtle" onClick={props.onAddSampleDocument}>
                Dodaj vzorčni dokument
              </button>
            </div>
          }
        >
          <div className="document-list">
            {props.documents.length === 0 ? (
              <div className="callout">
                <strong>Knjižnica je trenutno prazna.</strong>
                <p className="muted">
                  Dodaj prvi dokument, uvozi JSON stanje ali v pogledu Export / Import ponastavi
                  aplikacijo na vzorčne podatke.
                </p>
              </div>
            ) : (
              props.documents.map((document) => {
                const linkedCount = props.truthUnits.filter((unit) => unit.documentId === document.id).length;
                return (
                  <article key={document.id} className="document-item">
                    <div className="row start">
                      <div>
                        <strong>{document.title}</strong>
                        <div className="badge-row">
                          <span className="badge accent">{formatDate(document.updatedAt)}</span>
                          <span className="badge">{linkedCount} povezanih enot</span>
                          {document.filename ? <span className="badge">{document.filename}</span> : null}
                        </div>
                      </div>
                    </div>
                    <p className="muted">
                      {document.content.length > 240
                        ? `${document.content.slice(0, 240)}…`
                        : document.content}
                    </p>
                  </article>
                );
              })
            )}
          </div>
        </Panel>

        <Panel title="Ročni vnos dokumenta">
          <div className="stack">
            <div className="field">
              <label htmlFor="doc-title">Naslov dokumenta</label>
              <input
                id="doc-title"
                value={title}
                onChange={(event) => setTitle(event.target.value)}
                placeholder="Npr. Delovni zapis o definiciji resnice"
              />
            </div>
            <div className="field">
              <label htmlFor="doc-content">Vsebina</label>
              <textarea
                id="doc-content"
                value={content}
                onChange={(event) => setContent(event.target.value)}
                placeholder="Vnesi izsek dokumenta ali delovni zapis, ki bo postal vir za truth units."
              />
            </div>
            <div className="callout">
              Aplikacija iz dokumenta ne razglasi resnice sama. Najprej shrani vir, nato ročno
              uredi ali poveži enote resnice.
            </div>
            <div className="row start">
              <button className="primary" onClick={submit}>
                Shrani dokument
              </button>
            </div>
          </div>
        </Panel>
      </div>
    </div>
  );
}
