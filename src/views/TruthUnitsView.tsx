import { useState } from "react";

import { Panel } from "../components/Panel";
import {
  consentOptions,
  formatDate,
  relationTypeLabels,
  truthStatusOptions,
  truthTypeOptions,
  type ConsentStatus,
  type StudioState,
  type TruthStatus,
  type TruthType,
  type TruthUnit,
} from "../domain/types";

type TruthUnitsViewProps = {
  state: StudioState;
  selectedUnitId: string;
  onSelectUnit: (id: string) => void;
  onUpdateUnit: (id: string, patch: Partial<TruthUnit>) => void;
};

export function TruthUnitsView(props: TruthUnitsViewProps): JSX.Element {
  const [typeFilter, setTypeFilter] = useState<TruthType | "ALL">("ALL");
  const [statusFilter, setStatusFilter] = useState<TruthStatus | "ALL">("ALL");
  const [consentFilter, setConsentFilter] = useState<ConsentStatus | "ALL">("ALL");

  const resetFilters = (): void => {
    setTypeFilter("ALL");
    setStatusFilter("ALL");
    setConsentFilter("ALL");
  };

  const filteredUnits = props.state.truthUnits.filter((unit) => {
    return (
      (typeFilter === "ALL" || unit.type === typeFilter) &&
      (statusFilter === "ALL" || unit.status === statusFilter) &&
      (consentFilter === "ALL" || unit.consentStatus === consentFilter)
    );
  });

  const hasTruthUnits = props.state.truthUnits.length > 0;
  const hasFilteredUnits = filteredUnits.length > 0;

  const selectedUnit =
    filteredUnits.find((unit) => unit.id === props.selectedUnitId) ?? filteredUnits[0] ?? null;

  const selectedDocument = selectedUnit
    ? props.state.documents.find((document) => document.id === selectedUnit.documentId) ?? null
    : null;

  const selectedEvidence = selectedUnit
    ? props.state.evidenceRefs.filter((item) => item.truthUnitId === selectedUnit.id)
    : [];

  const selectedDefinitions = selectedUnit
    ? props.state.definitions.filter(
        (item) =>
          item.linkedUnitIds.includes(selectedUnit.id) || selectedUnit.keyDefinitions.includes(item.term),
      )
    : [];

  const selectedCounterAngle = selectedUnit
    ? props.state.counterAngles.find((item) => item.truthUnitId === selectedUnit.id) ?? null
    : null;

  const selectedLinks = selectedUnit
    ? props.state.links.filter(
        (link) => link.fromUnitId === selectedUnit.id || link.toUnitId === selectedUnit.id,
      )
    : [];

  return (
    <div className="view-grid">
      <Panel title="Truth Units tabela">
        {!hasTruthUnits ? (
          <div className="callout">
            <strong>Ni še enot resnice.</strong>
            <p className="muted">Najprej dodaj dokument ali uvozi obstoječe stanje.</p>
          </div>
        ) : (
          <>
            <div className="field-grid" style={{ marginBottom: "1rem" }}>
              <div className="field">
                <label htmlFor="filter-type">Filter po tipu</label>
                <select
                  id="filter-type"
                  value={typeFilter}
                  onChange={(event) => setTypeFilter(event.target.value as TruthType | "ALL")}
                >
                  <option value="ALL">Vsi tipi</option>
                  {truthTypeOptions.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              </div>
              <div className="field">
                <label htmlFor="filter-status">Filter po statusu</label>
                <select
                  id="filter-status"
                  value={statusFilter}
                  onChange={(event) => setStatusFilter(event.target.value as TruthStatus | "ALL")}
                >
                  <option value="ALL">Vsi statusi</option>
                  {truthStatusOptions.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              </div>
              <div className="field">
                <label htmlFor="filter-consent">Filter po soglasju</label>
                <select
                  id="filter-consent"
                  value={consentFilter}
                  onChange={(event) => setConsentFilter(event.target.value as ConsentStatus | "ALL")}
                >
                  <option value="ALL">Vsa soglasja</option>
                  {consentOptions.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            {!hasFilteredUnits ? (
              <div className="callout">
                <strong>Ni zadetkov za trenutni filter.</strong>
                <p className="muted">Spremeni filter ali prikaži vse enote.</p>
                <button type="button" className="subtle" style={{ marginTop: "0.85rem" }} onClick={resetFilters}>
                  Prikaži vse
                </button>
              </div>
            ) : (
              <table className="table">
                <thead>
                  <tr>
                    <th>Naslov</th>
                    <th>Tip</th>
                    <th>Status</th>
                    <th>Soglasje</th>
                    <th>Dokument</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredUnits.map((unit) => {
                    const documentTitle =
                      props.state.documents.find((document) => document.id === unit.documentId)?.title ?? "Neznan vir";
                    return (
                      <tr
                        key={unit.id}
                        className={unit.id === selectedUnit?.id ? "selected" : ""}
                        onClick={() => props.onSelectUnit(unit.id)}
                      >
                        <td>
                          <strong>{unit.title}</strong>
                          <div className="muted">{unit.claim}</div>
                        </td>
                        <td>{unit.type}</td>
                        <td>{unit.status}</td>
                        <td>{unit.consentStatus}</td>
                        <td>{documentTitle}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            )}
          </>
        )}
      </Panel>

      {selectedUnit ? (
        <div className="two-column">
          <Panel title="Editor enote">
            <div className="field-grid">
              <div className="field full">
                <label htmlFor="unit-title">Naslov enote</label>
                <input
                  id="unit-title"
                  value={selectedUnit.title}
                  onChange={(event) => props.onUpdateUnit(selectedUnit.id, { title: event.target.value })}
                />
              </div>
              <div className="field">
                <label htmlFor="unit-type">Tip</label>
                <select
                  id="unit-type"
                  value={selectedUnit.type}
                  onChange={(event) =>
                    props.onUpdateUnit(selectedUnit.id, {
                      type: event.target.value as TruthType,
                    })
                  }
                >
                  {truthTypeOptions.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              </div>
              <div className="field">
                <label htmlFor="unit-status">Status</label>
                <select
                  id="unit-status"
                  value={selectedUnit.status}
                  onChange={(event) =>
                    props.onUpdateUnit(selectedUnit.id, {
                      status: event.target.value as TruthStatus,
                    })
                  }
                >
                  {truthStatusOptions.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              </div>
              <div className="field">
                <label htmlFor="unit-consent">Moje soglasje</label>
                <select
                  id="unit-consent"
                  value={selectedUnit.consentStatus}
                  onChange={(event) =>
                    props.onUpdateUnit(selectedUnit.id, {
                      consentStatus: event.target.value as ConsentStatus,
                    })
                  }
                >
                  {consentOptions.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              </div>
              <div className="field full">
                <label htmlFor="unit-claim">Claim</label>
                <textarea
                  id="unit-claim"
                  value={selectedUnit.claim}
                  onChange={(event) => props.onUpdateUnit(selectedUnit.id, { claim: event.target.value })}
                />
              </div>
              <div className="field full">
                <label htmlFor="unit-notes">Opombe</label>
                <textarea
                  id="unit-notes"
                  value={selectedUnit.notes}
                  onChange={(event) => props.onUpdateUnit(selectedUnit.id, { notes: event.target.value })}
                />
              </div>
            </div>

            <div className="badge-row">
              <span className="badge accent">Posodobljeno {formatDate(selectedUnit.updatedAt)}</span>
              {selectedDocument ? <span className="badge">{selectedDocument.title}</span> : null}
            </div>
          </Panel>

          <div className="stack">
            <Panel title="Dokaz iz dokumenta">
              <div className="stack">
                {selectedEvidence.map((item) => (
                  <div key={item.id} className="meta-item">
                    <strong>{item.quote}</strong>
                    <div className="badge-row">
                      {item.sourceLocation ? <span className="badge">{item.sourceLocation}</span> : null}
                      <span className="badge good">zaupanje {Math.round(item.confidence * 100)}%</span>
                    </div>
                  </div>
                ))}
                {selectedUnit.evidenceFromDocument.map((entry) => (
                  <div key={entry} className="callout">
                    {entry}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel title="Definicije ključnih besed">
              <div className="meta-list">
                {selectedDefinitions.map((item) => (
                  <div key={item.id} className="meta-item">
                    <strong>{item.term}</strong>
                    <p className="muted">{item.definition}</p>
                    <span className="badge">{item.scope}</span>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel title="Proti-kot">
              <div className="meta-item">
                <strong>{selectedCounterAngle?.description ?? selectedUnit.counterAngle}</strong>
                <div className="badge-row">
                  <span className="badge warn">
                    resnost {selectedCounterAngle?.severity ?? "srednja"}
                  </span>
                </div>
              </div>
            </Panel>

            <Panel title="Predlagane povezave">
              <div className="meta-list">
                {selectedLinks.map((link) => (
                  <div key={link.id} className="meta-item">
                    <strong>
                      {props.state.truthUnits.find((unit) => unit.id === link.fromUnitId)?.title ?? "Vir"}{" "}
                      {relationTypeLabels[link.relationType]}{" "}
                      {props.state.truthUnits.find((unit) => unit.id === link.toUnitId)?.title ?? "Cilj"}
                    </strong>
                    <p className="muted">{link.note}</p>
                  </div>
                ))}
                {selectedUnit.proposedLinks.map((entry) => (
                  <div key={entry} className="callout">
                    {entry}
                  </div>
                ))}
              </div>
            </Panel>
          </div>
        </div>
      ) : null}
    </div>
  );
}
