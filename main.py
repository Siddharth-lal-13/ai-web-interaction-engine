# main.py

from vision.yolo_detector import YoloDetector
from audio.speech_to_text import SpeechToText
from automation.browser_controller import BrowserController


def main():
    # Initialize modules
    vision = YoloDetector()
    audio = SpeechToText()
    browser = BrowserController()

    # Example usage
    browser.open("https://example.com")

    # Take screenshot
    browser.screenshot("assets/page.png")

    # Run vision detection
    detections = vision.detect("assets/page.png")
    print("Detections:", detections)

    # Run speech-to-text
    text = audio.transcribe("assets/sample.wav")
    print("Transcription:", text)

    browser.close()


if __name__ == "__main__":
    main()
    