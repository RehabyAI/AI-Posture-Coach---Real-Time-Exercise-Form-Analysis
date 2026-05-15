import { useRef, useState } from "react";
import Webcam from "react-webcam";
import { X, Play, Square, Camera, Activity } from "lucide-react";

type Analysis = {
  posture: number;
  rangeOfMotion: number;
  symmetry: number;
  fatigue: string;
  status: string;
  feedback: string;
};

export function WebcamPanel({ onClose }: { onClose: () => void }) {
  const webcamRef = useRef<Webcam>(null);
  const [isRecording, setIsRecording] = useState(false);
  const [data, setData] = useState<Analysis | null>(null);

  const startAnalysis = () => {
    setIsRecording(true);
    setTimeout(() => {
      setData({
        posture: 87,
        rangeOfMotion: 92,
        symmetry: 78,
        fatigue: "Low",
        status: "Excellent Form",
        feedback:
          "Keep your spine straight. Slightly increase range of motion on the left side.",
      });
    }, 2000);
  };

  const stop = () => setIsRecording(false);
  const capture = () => {
    const src = webcamRef.current?.getScreenshot();
    if (src) console.log("Captured frame", src.slice(0, 40));
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 p-4">
      <div className="w-full max-w-5xl overflow-hidden rounded-2xl bg-card shadow-2xl">
        <div className="flex items-center justify-between bg-[image:var(--gradient-deep)] px-6 py-4 text-primary-foreground">
          <h2 className="flex items-center gap-2 text-lg font-semibold">
            <Activity className="h-5 w-5" /> Real-Time Movement Analysis
          </h2>
          <button
            onClick={onClose}
            aria-label="Close"
            className="grid h-9 w-9 place-items-center rounded-full bg-white/20 transition hover:bg-white/30"
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        <div className="grid gap-5 p-6 md:grid-cols-2">
          <div className="relative overflow-hidden rounded-xl bg-muted">
            <Webcam
              ref={webcamRef}
              audio={false}
              screenshotFormat="image/jpeg"
              className="h-full w-full object-cover"
              videoConstraints={{ facingMode: "user" }}
            />
            {isRecording && (
              <div className="absolute right-3 top-3 animate-pulse rounded-full bg-destructive px-3 py-1 text-xs font-bold text-destructive-foreground">
                ● ANALYZING
              </div>
            )}
          </div>

          <div className="max-h-[480px] overflow-y-auto rounded-xl bg-surface-soft p-5">
            {data ? (
              <div className="space-y-5">
                <h3 className="text-base font-semibold text-primary-deep">
                  Analysis Results
                </h3>
                {[
                  { label: "Posture Quality", value: data.posture },
                  { label: "Range of Motion", value: data.rangeOfMotion },
                  { label: "Symmetry", value: data.symmetry },
                ].map((m) => (
                  <div key={m.label}>
                    <div className="mb-1 flex justify-between text-sm font-medium">
                      <span>{m.label}</span>
                      <span>{m.value}%</span>
                    </div>
                    <div className="h-3 overflow-hidden rounded-full bg-card">
                      <div
                        className="h-full bg-[image:var(--gradient-primary)] transition-all"
                        style={{ width: `${m.value}%` }}
                      />
                    </div>
                  </div>
                ))}
                <div className="rounded-lg bg-card p-4 text-sm shadow-[var(--shadow-soft)]">
                  <div className="flex justify-between py-1">
                    <span className="text-muted-foreground">Fatigue</span>
                    <strong className="text-primary">{data.fatigue}</strong>
                  </div>
                  <div className="flex justify-between py-1">
                    <span className="text-muted-foreground">Status</span>
                    <strong className="text-primary">{data.status}</strong>
                  </div>
                </div>
                <div className="rounded-lg border border-primary/20 bg-card p-4">
                  <h4 className="mb-1 text-sm font-semibold text-primary-deep">
                    Feedback
                  </h4>
                  <p className="text-sm text-muted-foreground">{data.feedback}</p>
                </div>
              </div>
            ) : (
              <div className="grid h-full place-items-center text-center text-sm text-muted-foreground">
                <p>Press “Start Analysis” to see real-time metrics.</p>
              </div>
            )}
          </div>
        </div>

        <div className="flex flex-wrap justify-end gap-3 border-t border-border bg-background px-6 py-4">
          {!isRecording ? (
            <button
              onClick={startAnalysis}
              className="inline-flex items-center gap-2 rounded-full bg-primary px-5 py-2 text-sm font-semibold text-primary-foreground shadow-[var(--shadow-card)] transition hover:opacity-90"
            >
              <Play className="h-4 w-4" /> Start Analysis
            </button>
          ) : (
            <button
              onClick={stop}
              className="inline-flex items-center gap-2 rounded-full bg-destructive px-5 py-2 text-sm font-semibold text-destructive-foreground transition hover:opacity-90"
            >
              <Square className="h-4 w-4" /> Stop
            </button>
          )}
          <button
            onClick={capture}
            className="inline-flex items-center gap-2 rounded-full bg-accent px-5 py-2 text-sm font-semibold text-accent-foreground transition hover:opacity-90"
          >
            <Camera className="h-4 w-4" /> Capture
          </button>
          <button
            onClick={onClose}
            className="rounded-full border border-border bg-card px-5 py-2 text-sm font-medium text-foreground transition hover:bg-muted"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
