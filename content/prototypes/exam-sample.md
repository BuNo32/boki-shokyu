# 模擬試験見本（10分タイマー）

> 本番は第1問（用語）・第2問（仕訳）・第3問（試算表）の3パート想定。ここではサンプル問題（3問）でタイマー動作のみ確認します。

<div id="timer"></div>
<div id="exam-root">
  <div id="quiz-proto3"></div>
</div>

<script>
  // 外部スクリプト（quiz.js / exam.js）が読まれた後に実行されるように調整
  (function runWhenReady(cb){
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', cb, { once: true });
    } else {
      setTimeout(cb, 0);
    }
  })(function(){
    // タイマー開始（試験10分）
    if (typeof startTimer === 'function') {
      startTimer(600, 'timer', () => {
        // 時間切れで入力とボタンを無効化
        document
          .querySelectorAll('#exam-root input, #exam-root button')
          .forEach((el) => (el.disabled = true));
      });
    } else {
      console.warn('startTimer is not available yet');
    }

    // loadQuiz は遅延キューに積んでおく（quiz.js 読込後に処理）
    window.__loadQuizQueue = window.__loadQuizQueue || [];
    window.__loadQuizQueue.push([
      '../quizzes/prototype.json',
      'quiz-proto3',
      { quizId: 'proto' },
    ]);
  });
  </script>
