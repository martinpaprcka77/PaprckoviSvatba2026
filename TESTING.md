# 🧪 Testing Strategy

## Test Coverage

| Component | Type | Tests | Status |
|-----------|------|-------|--------|
| `parseBudgetMD()` | Unit | 4 | ✅ Pass |
| `parseGuestsMD()` | Unit | 2 | ✅ Pass |
| `parseTasksMD()` | Unit | 3 | ✅ Pass |
| Data integrity | Integration | 3 | ✅ Pass |
| **Total** | | **12** | **✅ Pass** |

## Running Tests

1. **In browser:** Open `tests.html` in your browser
   ```
   http://localhost:8000/tests.html
   ```

2. **What gets tested:**
   - Markdown parsing (all 3 formats)
   - Edge cases (empty data, missing fields, special sections)
   - Data integrity (budget sum, hard cap, non-empty lists)

## Test Cases

### parseBudgetMD()
- ✅ Parse valid budget table with prices
- ✅ Ignore "Rozpady" section (sub-items) — prevents double-counting
- ✅ Handle empty budget (no table)
- ✅ Skip CELKEM row (total row)

### parseGuestsMD()
- ✅ Parse guests by side (Mamka, Taťka, Společní)
- ✅ Handle missing data (?, _, empty cells)

### parseTasksMD()
- ✅ Parse valid task with deadline, title, assignee
- ✅ Detect done tasks `[x]` vs incomplete `[ ]`
- ✅ Handle empty tasks (no table)

### Data Integrity
- ✅ Budget total calculation is correct
- ✅ Hard cap (100 000 Kč) is respected
- ✅ Tasks list is never empty

## How to Add Tests

Edit `tests.html` → add new test:

```javascript
runner.test('Feature: What should happen', () => {
    // Setup
    const data = { ... };
    
    // Call function
    const result = parseX(data);
    
    // Assert
    runner.assertEqual(result.length, 5, 'Should have 5 items');
    runner.assert(result[0].price > 0, 'Price must be positive');
});
```

## Edge Cases Covered

| Scenario | Handled? | Test |
|----------|----------|------|
| Empty markdown | ✅ | Returns empty array |
| Missing cells | ✅ | Skips incomplete rows |
| Special sections (Rozpady) | ✅ | Stops parsing at `## Rozpady` |
| Unknown status markers | ✅ | Treats as incomplete |
| Budget over cap | ✅ | Still renders, marked red |

## Future Tests (TODO)

- [ ] localStorage save/load
- [ ] Offline mode (no network)
- [ ] Render functions (UI correctness)
- [ ] Browser compatibility (mobile vs desktop)
- [ ] Performance (large data sets)
- [ ] Accessibility (keyboard nav, screen readers)

## CI/CD Integration

**GitHub Actions:** Tests run automatically on PR
- Command: `npm test` or open `tests.html` in headless browser
- Currently: Manual via browser (no CI setup)

To automate: Add GitHub Actions workflow that opens `tests.html` in Puppeteer/Playwright.
