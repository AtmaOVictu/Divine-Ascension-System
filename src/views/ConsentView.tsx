import { Panel } from "../components/Panel";
import { consentOptions, type ConsentStatus, type TruthUnit } from "../domain/types";

type ConsentViewProps = {
  truthUnits: TruthUnit[];
  onConsentChange: (id: string, value: ConsentStatus) => void;
};

export function ConsentView(props: ConsentViewProps): JSX.Element {
  return (
    <div className="view-grid">
      <Panel title="Moje soglasje">
        <div className="callout" style={{ marginBottom: "1rem" }}>
          KANON ni avtomatski. Nastane samo takrat, ko ga uporabnik izrecno izbere v tem pogledu ali
          v editorju enote.
        </div>
        {props.truthUnits.length === 0 ? (
          <div className="callout">
            <strong>Ni še enot za potrditev.</strong>
            <p className="muted">
              Ko bodo ustvarjene enote resnice, se bodo tukaj pojavile možnosti za pregled in
              soglasje.
            </p>
          </div>
        ) : (
          <div className="status-grid">
            {props.truthUnits.map((unit) => (
              <article key={unit.id} className="status-item">
                <div className="row start">
                  <div>
                    <strong>{unit.title}</strong>
                    <p className="muted">{unit.claim}</p>
                  </div>
                </div>
                <div className="badge-row" style={{ marginBottom: "0.75rem" }}>
                  <span className="badge">{unit.type}</span>
                  <span className="badge accent">{unit.status}</span>
                </div>
                <select
                  value={unit.consentStatus}
                  onChange={(event) => props.onConsentChange(unit.id, event.target.value as ConsentStatus)}
                >
                  {consentOptions.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              </article>
            ))}
          </div>
        )}
      </Panel>
    </div>
  );
}
