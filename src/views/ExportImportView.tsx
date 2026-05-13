import { useRef, useState, type ChangeEvent } from "react";

import { Panel } from "../components/Panel";
import { formatDate } from "../domain/types";
import type { ImportMetadata } from "../store/localStore";

type ExportImportViewProps = {
  importMetadata: ImportMetadata | null;
  onExport: () => void;
  onImport: (text: string) => string;
  onReset: () => void;
};

function renderMetadataValue(value: string | null | undefined): string {
  return value && value.trim().length > 0 ? value : "Unavailable";
}

export function ExportImportView(props: ExportImportViewProps): JSX.Element {
  const [message, setMessage] = useState("JSON paket vsebuje dokumente, enote, definicije, povezave in simulacije.");
  const fileRef = useRef<HTMLInputElement | null>(null);

  const handleImport = async (event: ChangeEvent<HTMLInputElement>): Promise<void> => {
    const file = event.target.files?.[0];

    if (!file) {
      return;
    }

    const content = await file.text();
    const result = props.onImport(content);
    setMessage(result);
    event.target.value = "";
  };

  return (
    <div className="view-grid">
      <div className="two-column">
        <Panel title="Export JSON">
          <div className="stack">
            <p className="muted">
              Izvoz shrani lokalni studio v en sam JSON paket. Uporabno za arhiv ali prenos med
              lokalnimi primeri.
            </p>
            <div className="row start">
              <button className="primary" onClick={props.onExport}>
                Exportiraj JSON
              </button>
              <button className="subtle" onClick={props.onReset}>
                Ponastavi na vzorčne podatke
              </button>
            </div>
            <div className="callout">
              Prazno stanje ni napaka. Je začetna osnova. Za demo vsebino uporabi ponastavitev na
              vzorčne podatke.
            </div>
          </div>
        </Panel>

        <Panel title="Import JSON">
          <div className="stack">
            <div className="import-box">
              <p className="muted">
                Uvozi predhodno izvožen JSON. Po uvozu se stanje takoj zapiše v localStorage in
                ostane po refreshu.
              </p>
              <div className="row start">
                <button onClick={() => fileRef.current?.click()}>Izberi JSON datoteko</button>
                <input
                  ref={fileRef}
                  type="file"
                  accept="application/json"
                  hidden
                  onChange={handleImport}
                />
              </div>
            </div>
            <div className="callout">{message}</div>
            {props.importMetadata ? (
              <div className="stack">
                <div className="callout">
                  To je import source metadata. Ni kanon in ne predstavlja avtomatske potrditve.
                </div>

                {props.importMetadata.importKind === "envelope" ? (
                  <div className="meta-list">
                    <div className="meta-item">
                      <strong>Contract</strong>
                      <div className="muted">{props.importMetadata.contract}</div>
                    </div>
                    <div className="meta-item">
                      <strong>Generated</strong>
                      <div className="muted">
                        {props.importMetadata.generatedAt
                          ? formatDate(props.importMetadata.generatedAt)
                          : "Unavailable"}
                      </div>
                    </div>
                    <div className="meta-item">
                      <strong>Layer</strong>
                      <div className="muted">{renderMetadataValue(props.importMetadata.source?.layer)}</div>
                    </div>
                    <div className="meta-item">
                      <strong>Generator</strong>
                      <div className="muted">{renderMetadataValue(props.importMetadata.source?.generator)}</div>
                    </div>
                    <div className="meta-item">
                      <strong>Adapter</strong>
                      <div className="muted">{renderMetadataValue(props.importMetadata.source?.adapter)}</div>
                    </div>
                    <div className="meta-item">
                      <strong>Input Artifact</strong>
                      <div className="muted">{renderMetadataValue(props.importMetadata.source?.inputArtifact)}</div>
                    </div>
                    <div className="meta-item">
                      <strong>Mode</strong>
                      <div className="muted">{renderMetadataValue(props.importMetadata.source?.mode)}</div>
                    </div>
                    <div className="meta-item">
                      <strong>Manual Canon Gate</strong>
                      <div className="muted">{renderMetadataValue(props.importMetadata.source?.manualCanonGate)}</div>
                    </div>
                  </div>
                ) : (
                  <div className="meta-item">
                    <strong>Direct StudioState import</strong>
                    <p className="muted">
                      Zadnji uvoz je bil neposreden `StudioState` paket brez envelope provenance.
                    </p>
                  </div>
                )}
              </div>
            ) : null}
          </div>
        </Panel>
      </div>
    </div>
  );
}
